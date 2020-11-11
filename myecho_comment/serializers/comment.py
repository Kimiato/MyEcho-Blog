from rest_framework import serializers

from myecho_comment.models import Comment
from myecho.utils.rest_serializers import BaseModelSerializer


class CommentSerializer(BaseModelSerializer):
    """
        评论serializer
    """

    class Meta(BaseModelSerializer.Meta):
        model = Comment
        exclude = BaseModelSerializer.Meta.exclude + ['user_ip', 'user']