from rest_framework import pagination
from django.utils.translation import gettext_lazy as _


class BasePageNumberPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_description = _('可以添加no_page不分页')
    page_size_query_description = _('数据量过大时请勿使用no_page')

    def paginate_queryset(self, queryset, request, view=None):
        if 'no_page' in request.query_params:
            return None
        return super(BasePageNumberPagination, self).paginate_queryset(queryset, request, view)
