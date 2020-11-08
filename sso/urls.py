from rest_framework import routers
from django.conf.urls import url, include

from sso.endpoints import (
    AuthTokenApiView,
    UserViewSet
)

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', AuthTokenApiView.as_view(), name='auth')
]