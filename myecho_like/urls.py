from rest_framework import routers
from django.conf.urls import url, include

from myecho_like.endpoints import (
    CommentLikeViewSet,
    ArticleLikeViewset
)


router = routers.SimpleRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^comment/like/', CommentLikeViewSet.as_view(), name='comment-like'),
    url(r'^article/like/', ArticleLikeViewset.as_view(), name='article-like')
]