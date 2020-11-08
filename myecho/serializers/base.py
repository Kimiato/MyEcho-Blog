from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['is_deleted']
        read_only_fields = ['create_time', 'update_time']