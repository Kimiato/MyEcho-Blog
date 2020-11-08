from django.db import models

from myecho.db.models import BaseModel


class Classification(BaseModel):

    class Meta:
        db_table = 'myecho_classification'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    name = models.CharField(verbose_name='分类名', help_text='分类名', max_length=64)
    father_classification = models.ForeignKey(to='self', verbose_name='父级分类', on_delete=models.CASCADE, null=True)
