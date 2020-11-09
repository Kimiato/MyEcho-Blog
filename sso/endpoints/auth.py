from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from myecho.utils.rest_views import BaseApiView
from sso.serializers import AuthTokenSerializer, UserSerializer, TokenSerializer
from sso.controllers import authenticate
from sso.models import Token

class AuthTokenApiView(BaseApiView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
            # 验证用户账号密码, 获取token
                request data:
                {
                    "username": str,
                    "password": str
                }
                response data:
                {
                    "token": str,
                    "expires_time": datetime  # 过期时间
                }
            # 使用方式:
                在请求的header里面添加

                Authorization Token token
        """
        auth_token_serializer = AuthTokenSerializer(data=request.data)
        if not auth_token_serializer.is_valid():
            return JsonResponse(auth_token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = auth_token_serializer.validated_data['username']
        password = auth_token_serializer.validated_data['password']
        user = authenticate(username, password)
        if not user:
            raise AuthenticationFailed()
        token, _ = Token.objects.get_or_create(user=user)
        token.save()
        user_serializer = UserSerializer(instance=user)
        token_serializer = TokenSerializer(instance=token)
        data = {
            'token': token_serializer.data,
            'user': user_serializer.data
        }
        return JsonResponse(data)