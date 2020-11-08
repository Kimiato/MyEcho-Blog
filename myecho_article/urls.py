from rest_framework import routers
from django.conf.urls import url, include

from myecho_article.endpoints import ArticleViewSet

router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]