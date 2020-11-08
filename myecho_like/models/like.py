from django.db import models

from myecho.db.models import BaseModel
from myecho_article.models import Article
from myecho_comment.models import Comment


class Like(BaseModel):
    """
        点赞基类
    """
    class Meta:
        abstract = True

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    like_from_ip = models.IPAddressField(verbose_name='点赞ip')
    is_positive = models.BooleanField(verbose_name='点赞/踩', default=True)


class CommentLike(Like):
    """
        评论点赞
    """
    class Meta:
        db_table = 'myecho_comment_like'

    comment = models.ForeignKey(Comment, verbose_name='评论外键关联', on_delete=models.CASCADE)


class ArticleLike(Like):
    """
        文章点赞
    """
    class Meta:
        db_table = 'myecho_article_like'

    article = models.ForeignKey(Article, verbose_name='文章外键关联', on_delete=models.CASCADE)