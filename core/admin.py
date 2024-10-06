from django.contrib import admin

# Register your models here.
from core.models import Writer


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_editor', 'date_joined', 'last_login')
    list_filter = ('is_editor',)
    search_fields = ('name',)
    ordering = ('-date_joined',)