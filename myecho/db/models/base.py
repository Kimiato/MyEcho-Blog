from django.db import models

from .query import SoftDeletableQuerySet


# 软删除manager
class SoftDeletableManagerMixin(object):
    """
    Manager that limits the queryset by default to show only not deleted
    instances of model.
    """
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        """
        Return queryset limited to not deleted entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_deleted=False)


class SoftDeletableManager(SoftDeletableManagerMixin, models.Manager):
    pass


class BaseModel(models.Model):
    """
        使用了软删除的BaseModel
    """
    class Meta:
        abstract = True

    create_time = models.DateTimeField(db_column='create_time', auto_now_add=True)
    update_time = models.DateTimeField(db_column='update_time', auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeletableManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        Soft delete object (set its ``is_deleted`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(BaseModel, self).delete(using=using, *args, **kwargs)