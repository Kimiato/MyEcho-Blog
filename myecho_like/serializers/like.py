from myecho.utils.rest_serializers import BaseModelSerializer
from myecho_like.models import CommentLike, ArticleLike


class CommentLikeSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = CommentLike
        exclude = BaseModelSerializer.Meta.exclude + ['like_from_ip']


class ArticleLikeSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = ArticleLike
        exclude = BaseModelSerializer.Meta.exclude + ['like_from_ip']
