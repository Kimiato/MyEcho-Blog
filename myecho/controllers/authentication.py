from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import ugettext_lazy as _
from functools import update_wrapper
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header

from sso.models import Token


class AuthUser:
    def __init__(self, username, is_authenticated, is_anonymous) -> None:
        self.id = id
        self.username = username
        self.is_authenticated = is_authenticated
        self.is_anonymous = is_anonymous


def action_authentication(*authentications, validate_authentication=True):
    """
        接口级别的权限装饰器
    """
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            self.authentication_classes = authentications
            if validate_authentication:
                authenticators = self.get_authenticators()
                for authenticator in authenticators:
                    authenticator.authenticate(request)
            return func(self, request, *args, **kwargs)
        return update_wrapper(wrapper, func)
    return decorator


class BaseTokenAuthentication(TokenAuthentication):
    """
        基础Token验证登录认证
    """
    model = Token

    def authenticate(self, request):
        self.request = request
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            raise AuthenticationFailed(_('未登录！'))

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def _get_user_by_token_key(self, key):
        token = Token.objects.filter(key=key).first()
        if token:
            if token.is_expired:
                raise AuthenticationFailed(_('过期的 token.'))
            user = token.user
        else:
            raise AuthenticationFailed(_('错误的 token.'))
        setattr(self.request, 'user', user)
        return user, token

    def authenticate_credentials(self, key):
        user, token = self._get_user_by_token_key(key)
        return (user, token)