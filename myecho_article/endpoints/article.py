from rest_framework.response import Response

from myecho.utils.rest_views import BaseModelViewSet
from myecho.controllers.authentication import action_authentication, BaseTokenAuthentication
from myecho.controllers.permissions import action_permission, IsAuthor
from myecho_article.models import Article, ArticleDetail
from myecho_article.serializers import (
    ArticleSerializer,
    ArticleListSerializer,
)


class ArticleViewSet(BaseModelViewSet):
    """
        文章 ViewSet
    """
    authentication_classes = []
    permission_classes = []
    queryset = Article.objects.order_by('id')
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        """
            # 文章列表
        """
        self.serializer_class = ArticleListSerializer
        return super(ArticleViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            # 文章详情
        """
        instance = self.get_object()
        read_count = instance.read_count + 1
        Article.objects.filter(id=instance.id).update(read_count=read_count)
        return super(ArticleViewSet, self).retrieve(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAuthor)
    def destroy(self, request, *args, **kwargs):
        """
            # 删除文章
        """
        return super(ArticleViewSet, self).destroy(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    def create(self, request, *args, **kwargs):
        """
            创建文章
        """
        return super(ArticleViewSet, self).create(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAuthor)
    def update(self, request, *args, **kwargs):
        """
            更新文章
        """
        return super(ArticleViewSet, self).update(request, *args, **kwargs)

    def perform_create(self, serializer):
        data = serializer.validated_data
        data.update(user=self.request.user)
        super(ArticleViewSet, self).perform_create(serializer)