from django.db import models

from core.abstracts import AuditTrailModel
from blog.models.field_choices import ArticleStatus


class ArticleStatus(models.TextChoices):
    INACTIVE = "inactive"
    # ->
    PENDING_APPROVAL = 'pending_approval'
    # ->
    APPROVED = "approved"
    # ->
    REJECTED = "rejected"
    # ->
    QUEUED = 'queued'
    # ->
    PUBLISHED = "published"


class Article(AuditTrailModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(choices=ArticleStatus.choices, default=ArticleStatus.INACTIVE, max_length=20)
    written_by = models.ForeignKey("core.Writer", on_delete=models.CASCADE, related_name='writer_articles')
    edited_by = models.ForeignKey("core.Writer", on_delete=models.CASCADE, related_name='editor_articles', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

