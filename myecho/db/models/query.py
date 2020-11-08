from django.db import models
from django.db.models.query import QuerySet


# 自定义软删除查询基类
class SoftDeletableQuerySetMixin(object):
    """
    QuerySet for SoftDeletableModel. Instead of removing instance sets
    its ``is_deleted`` field to True.
    """

    def delete(self):
        """
        Soft delete objects from queryset (set their ``is_deleted``
        field to True)
        """
        self.update(is_deleted=True)


class SoftDeletableQuerySet(SoftDeletableQuerySetMixin, QuerySet):
    pass
