from rest_framework import serializers

from blog.models import Article, ArticleStatus
from core.models import Writer


class ArticleSummarySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    total_articles = serializers.IntegerField()
    articles_last_30 = serializers.IntegerField()


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']


class ArticleApproveSerializer(serializers.ModelSerializer):
    status = serializers.CharField()


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def create(self, validated_data):
        writer = self.context['request'].user
        validated_data.update({'status': ArticleStatus.PENDING_APPROVAL})
        return Article.objects.create(written_by=writer, **validated_data)


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name']


class ArticleApprovalSerializer(ArticleDetailSerializer):

    written_by = WriterSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'written_by', 'created_at', 'status']
