from django.contrib import admin

# Register your models here.

from blog.models import Article
from core.models import Writer


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'written_by', 'edited_by', 'created_at', 'updated_at')
    list_filter = ('status', 'written_by', 'edited_by')
    search_fields = ('title', 'written_by__name', 'edited_by__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


