from rest_framework import routers
from django.conf.urls import url, include


router = routers.SimpleRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
]