from rest_framework.permissions import BasePermission
from functools import update_wrapper


def action_permission(*permissions, validate_permission=True):
    """
        接口级别的认证装饰器
    """
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            self.permission_classes = permissions
            if validate_permission:
                self.check_permissions(request)
            return func(self, request, *args, **kwargs)
        return update_wrapper(wrapper, func)
    return decorator


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.permission_type == 0:
            return True
        return False