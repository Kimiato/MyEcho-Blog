from django.db import models

from myecho.db.models import BaseModel
from sso.models import User
from myecho_article.models import Article


class Comment(BaseModel):
    """
        评论
    """
    class Meta:
        db_table = 'myecho_comment'

    id = models.AutoField('id', primary_key=True, editable=False, help_text='主键')
    user = models.ForeignKey(User, verbose_name='评论人', on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(verbose_name='评论人姓名', max_length=50)
    user_ip = models.GenericIPAddressField(verbose_name='评论人ip')
    user_site = models.CharField(verbose_name='评论人网站', max_length=128, null=True)
    user_email = models.EmailField(verbose_name='评论人邮箱', null=True)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    father_comment = models.ForeignKey(to='self', verbose_name='父级评论', on_delete=models.SET_NULL, null=True)
    content = models.CharField(verbose_name='评论内容', max_length=512)
    is_examine = models.BooleanField(verbose_name="是否已经审核", default=0)