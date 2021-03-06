# Generated by Django 3.1.3 on 2020-11-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myecho_comment', '0001_initial'),
        ('myecho_article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time')),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(editable=False, help_text='主键', primary_key=True, serialize=False, verbose_name='id')),
                ('like_from_ip', models.GenericIPAddressField(verbose_name='点赞ip')),
                ('is_positive', models.BooleanField(default=True, verbose_name='点赞/踩')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myecho_comment.comment', verbose_name='评论外键关联')),
            ],
            options={
                'db_table': 'myecho_comment_like',
            },
        ),
        migrations.CreateModel(
            name='ArticleLike',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time')),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(editable=False, help_text='主键', primary_key=True, serialize=False, verbose_name='id')),
                ('like_from_ip', models.GenericIPAddressField(verbose_name='点赞ip')),
                ('is_positive', models.BooleanField(default=True, verbose_name='点赞/踩')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myecho_article.article', verbose_name='文章外键关联')),
            ],
            options={
                'db_table': 'myecho_article_like',
            },
        ),
    ]
