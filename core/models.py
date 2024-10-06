from django.db import models
from django.contrib.auth.models import AbstractUser
from core.abstracts import AuditTrailModel


class Writer(AbstractUser, AuditTrailModel):
    name = models.CharField(max_length=255)
    is_editor = models.BooleanField(default=False)

    @property
    def is_editor_by_permission(self):
        return self.groups.filter(name='Editor').exists()

    def __str__(self):
        return self.name
