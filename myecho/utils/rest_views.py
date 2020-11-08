from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins


class BaseModelViewSet(viewsets.ModelViewSet):
    pass


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    pass


class BaseApiView(APIView):
    pass


class BaseGenericViewSet(viewsets.GenericViewSet):
    pass


class BaseCreateModelMixin(mixins.CreateModelMixin):
    pass


class BaseDestroyModelMixin(mixins.DestroyModelMixin):
    pass


class BaseListModelMixin(mixins.ListModelMixin):
    pass


class BaseRetrieveModelMixin(mixins.RetrieveModelMixin):
    pass


class BaseUpdateModelMixin(mixins.UpdateModelMixin):
    pass