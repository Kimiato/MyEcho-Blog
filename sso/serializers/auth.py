from rest_framework import serializers


class AuthTokenSerializer(serializers.Serializer):
    """
        登录Serializer
    """
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, max_length=100)
