from rest_framework.views import Response
from rest_framework import status
from django.http import JsonResponse

from myecho.utils.rest_views import (
    BaseApiView,
)
from myecho.utils.toolfuns import get_client_ip
from myecho_like.serializers import (
    ArticleLikeSerializer,
    CommentLikeSerializer
)
from myecho_like.models import (
    ArticleLike,
    CommentLike
)


class CommentLikeViewSet(BaseApiView):

    def post(self, request):
        """
            # 评论点赞/踩
            ## request data:
                comment_id: int,
                is_positive: bool, 点赞/踩
        """
        data = request.data
        comment_like_serializer = CommentLikeSerializer(data=data)
        if not comment_like_serializer.is_valid():
            return JsonResponse(comment_like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_ip = get_client_ip(self.request)
        comment_id = comment_like_serializer.validated_data.get('comment_id')
        comment_like = CommentLike.objects.filter(like_from_ip=user_ip, comment_id=comment_id).first()
        if comment_like:
            return Response({'detail': '你已经点过赞/踩啦'})

        return Response({'detail': '成功'}, status=status.HTTP_201_CREATED)


class ArticleLikeViewset(BaseApiView):

    def post(self, request):
        """
            # 文章点赞/踩
            ## request data:
                article_id: int,
                is_positive: bool, 点赞/踩
        """
        data = request.data
        article_like_serializer = ArticleLikeSerializer(data=data)
        if not article_like_serializer.is_valid():
            return JsonResponse(article_like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_ip = get_client_ip(self.request)
        article_id = article_like_serializer.validated_data.get('comment_id')
        comment_like = ArticleLike.objects.filter(like_from_ip=user_ip, article_id=article_id).first()
        if comment_like:
            return Response({'detail': '你已经点过赞/踩啦'})

        return Response({'detail': '成功'}, status=status.HTTP_201_CREATED)