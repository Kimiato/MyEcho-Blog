from django.db import models

from myecho_article.models import Article
from myecho.db.models import BaseModel


class Tag(BaseModel):
    """
        文章标签
    """
    class Meta:
        db_table = 'myecho_tag'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    name = models.CharField(verbose_name='标签名字', max_length=32)
    articles = models.ManyToManyField(Article, related_name='articles', verbose_name='文章', null=True)

    def __str__(self) -> str:
        return self.name