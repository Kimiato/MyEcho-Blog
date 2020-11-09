from django.db import models
from myecho.db.models import BaseModel
from sso.models import User
from .classfication import Classification


class Article(BaseModel):
    """
        文章
    """
    class Meta:
        db_table = 'myecho_article'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    title = models.CharField(verbose_name='标题', help_text='文章标题', max_length=64)
    user = models.ForeignKey(User, verbose_name='作者', related_name='user', on_delete=models.CASCADE, editable=False)
    summary = models.CharField(verbose_name='摘要', help_text='文章摘要', max_length=255, null=True, editable=False)
    read_count = models.IntegerField(verbose_name='浏览量', default=0, editable=False)
    like_count = models.IntegerField(verbose_name='点赞数', help_text='点赞数', default=0, editable=False)
    comment_count = models.IntegerField(verbose_name='评论数', help_text='评论数', default=0, editable=False)
    classification = models.ForeignKey(Classification, verbose_name='分类', on_delete=models.SET_NULL, null=True)
    is_essence = models.BooleanField(verbose_name='是否精华', default=False)
    is_top = models.BooleanField(verbose_name='是否置顶', default=False)
    allow_comment = models.BooleanField(verbose_name='是否允许评论', default=True)

    def __str__(self) -> str:
        return self.title


class ArticleDetail(BaseModel):
    """
        文章详情
    """
    class Meta:
        db_table = 'myecho_article_detail'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    article = models.OneToOneField(Article, verbose_name='文章', on_delete=models.CASCADE, editable=False)
    content = models.TextField(verbose_name='文章内容', null=True)