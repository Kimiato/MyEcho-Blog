from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import ugettext_lazy as _
from functools import update_wrapper

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
        return super().authenticate(request)

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