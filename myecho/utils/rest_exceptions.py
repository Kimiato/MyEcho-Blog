from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class WrongOldPassword(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('旧密码错误.')
    default_code = 'Forbidden'