from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from myecho.utils.rest_views import BaseModelViewSet
from sso.models import User
from sso.serializers import UserSerializer


class UserViewSet(BaseModelViewSet):

    permission_classes = []
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @action(methods=['post'], detail=True)
    def rest_password(self, request, pk):
        """
            重置密码
            request data: {
                "password": str,
                "old_password": str, # 旧密码
            }
        """
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        pass

    def create(self, request, *args, **kwargs):
        """
            注册账号
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
