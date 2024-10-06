from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from blog.models import Article, ArticleStatus
from blog.serializers import ArticleSummarySerializer, ArticleCreateSerializer, ArticleDetailSerializer, \
    ArticleApprovalSerializer
from core.models import Writer
from core.permissions import HasEditorPermission


class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        last_30_days_articles_filter = Q(writer_articles__created_at__gte=timezone.now() - timezone.timedelta(days=30))

        writers = Writer.objects.annotate(
            total_articles=Count('writer_articles'),
            articles_last_30=Count('writer_articles', filter=last_30_days_articles_filter)
        )

        serializer = ArticleSummarySerializer(writers, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class_write = ArticleCreateSerializer
    serializer_class_read = ArticleDetailSerializer
    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return self.serializer_class_write

        return self.serializer_class_read

    def create(self, request, *args, **kwargs):
        serializer = ArticleCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED,)

    def get_queryset(self):
        # Ensure that only the writer can access their own articles
        return self.queryset.filter(written_by=self.request.user)


class ArticleApprovalViewSet(viewsets.GenericViewSet):
    permission_classes = [HasEditorPermission]
    serializer_class = ArticleApprovalSerializer

    def list(self, request):
        # Only show articles with status 'pending_approval'
        articles = Article.objects.filter(status=ArticleStatus.PENDING_APPROVAL)
        serializer = self.serializer_class(articles, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)

        article_status = request.data.get('status')
        if article_status not in (ArticleStatus.APPROVED, ArticleStatus.REJECTED):
            return Response({'status': 'Invalid Article Status'}, status=status.HTTP_400_BAD_REQUEST)

        article.status = article_status
        article.edited_by = request.user
        article.save()
        serializer = self.serializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesEditorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [HasEditorPermission]
    serializer_class = ArticleApprovalSerializer

    def get_queryset(self):
        return Article.objects.filter(edited_by=self.request.user)
