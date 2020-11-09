from myecho.utils.rest_serializers import BaseModelSerializer
from myecho_article.models import Article, ArticleDetail


class ArticleDetailSerializer(BaseModelSerializer):
    """
        文章详情serializer
    """
    class Meta(BaseModelSerializer.Meta):
        model = ArticleDetail


class ArticleSerializer(BaseModelSerializer):
    """
        文章serializer
    """
    article_detail = ArticleDetailSerializer(required=True, help_text="文章详情")

    class Meta(BaseModelSerializer.Meta):
        model = Article

    def create(self, validated_data):
        article_detail = validated_data.pop('article_detail')
        validated_data['summary'] = f"{article_detail['content'][:251]}..."
        instance = super(ArticleSerializer, self).create(validated_data)
        article_detail['article_id'] = instance.id
        article_detail_instance = ArticleDetail(**article_detail)
        article_detail_instance.save()
        return instance

    def update(self, instance, validated_data):
        article_detail = validated_data.get('article_detail')
        validated_data['summary'] = f"{article_detail['content'][:251]}..."
        article_detail_instance = ArticleDetail.objects.get(article=instance)
        article_detail_serializer = ArticleDetailSerializer(data=article_detail)
        article_detail_serializer.is_valid()
        article_detail_serializer.update(article_detail_instance, article_detail_serializer.validated_data)
        return super(ArticleSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        article_detail = ArticleDetail.objects.get(article=instance)
        if not hasattr(instance, 'article_detail'):
            setattr(instance, 'article_detail', article_detail)

        return super(ArticleSerializer, self).to_representation(instance)

class ArticleListSerializer(BaseModelSerializer):
    """
        文章列表serializer
    """
    class Meta(BaseModelSerializer.Meta):
        model = Article