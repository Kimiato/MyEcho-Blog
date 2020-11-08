from myecho.serializers import BaseModelSerializer
from sso.models import Token


class TokenSerializer(BaseModelSerializer):
    class Meta:
        model = Token
        exclude = []