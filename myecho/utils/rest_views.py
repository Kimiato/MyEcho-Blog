from rest_framework.views import APIView
from rest_framework import viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    pass


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    pass


class BaseApiView(APIView):
    pass
