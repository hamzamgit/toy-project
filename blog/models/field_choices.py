from django.db import models


class ArticleStatus(models.TextChoices):
    INACTIVE = "inactive", "INACTIVE"
    # ->
    PENDING_APPROVAL = 'pending_approval', "PENDING_APPROVAL"
    # ->
    APPROVED = "approved", "APPROVED"
    # ->
    REJECTED = "rejected", "REJECTED"
    # ->
    QUEUED = 'queued', "QUEUED"
    # ->
    PUBLISHED = "published", "PUBLISHED"
