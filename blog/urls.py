"""
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.viewsets import DashboardViewSet, ArticleViewSet, ArticleApprovalViewSet, ArticlesEditorViewSet

router = DefaultRouter()

router.register(r'dashboard', DashboardViewSet, basename='dashboard')
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'articles_approval', ArticleApprovalViewSet, basename='article_approval')
router.register(r'articles_editor', ArticlesEditorViewSet, basename='articles_editor')

urlpatterns = [
    path('', include(router.urls)),
]
