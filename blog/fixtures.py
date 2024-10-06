import pytest
from django.contrib.auth.models import Group

from blog.models import Article, ArticleStatus
from core.models import Writer
from django.utils import timezone
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def editor_group():
    return Group.objects.create(name="Editor")


@pytest.fixture
def editor_writer(editor_group):
    writer = Writer.objects.create_user(username="editor_user", password="editor_pass", is_editor=True)
    writer.groups.add(editor_group)
    return writer


@pytest.fixture
def normal_writer():
    return Writer.objects.create_user(username="writer_user", password="writer_pass", is_editor=False)


@pytest.fixture
def article_pending(normal_writer):
    return Article.objects.create(
        title="Pending Article",
        content="Pending content",
        status=ArticleStatus.PENDING_APPROVAL,
        written_by=normal_writer
    )


@pytest.fixture
def article_approved(editor_writer):
    return Article.objects.create(
        title="Approved Article",
        content="Approved content",
        status=ArticleStatus.APPROVED,
        written_by=editor_writer,
        edited_by=editor_writer,
        created_at=timezone.now()
    )
