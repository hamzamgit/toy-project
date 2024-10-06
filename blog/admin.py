from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'written_by', 'edited_by', 'created_at')
    list_filter = ('status', 'written_by', 'edited_by')
    search_fields = ('title', 'written_by__name', 'edited_by__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


