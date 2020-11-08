from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins


class BaseGenericViewSet(viewsets.GenericViewSet):

    def perform_authentication(self, request):
        super(BaseGenericViewSet, self).perform_authentication(request)


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


class BaseModelViewSet(BaseCreateModelMixin,
                       BaseRetrieveModelMixin,
                       BaseUpdateModelMixin,
                       BaseDestroyModelMixin,
                       BaseListModelMixin,
                       BaseGenericViewSet,):
    pass


class BaseReadOnlyModelViewSet(BaseRetrieveModelMixin, BaseListModelMixin, BaseGenericViewSet):
    pass


class BaseApiView(APIView):
    pass
