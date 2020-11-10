from rest_framework import routers
from django.conf.urls import url, include

from myecho_comment.endpoints import CommentViewSet


router = routers.SimpleRouter()

router.register('comments', CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]