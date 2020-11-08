from sso.models import User
from myecho.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        exclude = ['create_time', 'update_time', 'password', 'last_login']