from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from myecho.utils.rest_views import (
    BaseGenericViewSet,
    BaseCreateModelMixin,
    BaseDestroyModelMixin,
    BaseRetrieveModelMixin,
    BaseListModelMixin
)
from myecho.controllers import BaseTokenAuthentication, action_permission, action_authentication, IsAdmin
from sso.models import User
from sso.serializers import UserSerializer
from myecho.utils.rest_exceptions import WrongOldPassword


class UserViewSet(BaseGenericViewSet,
                BaseCreateModelMixin,
                BaseListModelMixin,
                BaseDestroyModelMixin,
                BaseRetrieveModelMixin):

    authentication_classes = []
    permission_classes = []
    queryset = User.objects.order_by('id')
    serializer_class = UserSerializer

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    def destroy(self, request, *args, **kwargs):
        """
            # 删除账号
        """
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    def list(self, request, *args, **kwargs):
        """
            # 已注册账号列表
        """
        return super(UserViewSet, self).list(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    def retrieve(self, request, *args, **kwargs):
        """
            # 账号详情
        """
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            # 注册账号
        """
        raw_password = request.data.get('password')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        instance = serializer.instance
        instance.set_password(raw_password)
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action_authentication(BaseTokenAuthentication)
    @action(methods=['post'], detail=False)
    def rest_password(self, request):
        """
            # 重置密码
            request data: {
                "password": str,
                "old_password": str, # 旧密码
            }
        """
        user = self.request.user
        password = request.data.get('password')
        old_password = request.data.get('old_password')
        if not user.check_password(old_password):
            raise WrongOldPassword()
        user.set_password(password)
        user.save()
        return Response({"detail": "密码修改成功"}, status=status.HTTP_200_OK)