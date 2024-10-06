from django.db import models


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
