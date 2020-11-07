from myecho.serializer import BaseModelSerializer
from sso.models import Token


class TokenSerializer(BaseModelSerializer):
    class Meta:
        model = Token
        exclude = []