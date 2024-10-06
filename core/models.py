from django.db import models
from django.contrib.auth.models import AbstractUser
from core.abstracts import AuditTrailModel


class Writer(AbstractUser, AuditTrailModel):
    name = models.CharField(max_length=255)
    is_editor = models.BooleanField(default=False)

    def __str__(self):
        return self.name
