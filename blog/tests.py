import pytest
from rest_framework import status
from blog.models import Article, ArticleStatus
from blog.fixtures import (
    api_client, normal_writer,
    article_pending, article_approved,
    editor_writer, editor_group

)

@pytest.mark.django_db
def test_create_article(api_client, normal_writer):
    api_client.force_authenticate(normal_writer)

    payload = {
        "title": "New Article",
        "content": "New article content",
    }

    response = api_client.post("/api/article/", data=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Article.objects.count() == 1
    assert Article.objects.get().title == "New Article"


@pytest.mark.django_db
def test_approve_article(api_client, editor_writer, article_pending):
    api_client.force_authenticate(editor_writer)

    payload = {
        "status": "approved"
    }

    response = api_client.put(f"/api/articles_approval/{article_pending.id}/", data=payload)

    assert response.status_code == status.HTTP_200_OK
    article_pending.refresh_from_db()
    assert article_pending.status == ArticleStatus.APPROVED
    assert article_pending.edited_by == editor_writer


@pytest.mark.django_db
def test_view_edited_articles(api_client, editor_writer, article_approved):
    api_client.force_authenticate(editor_writer)

    response = api_client.get("/api/articles_editor/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == article_approved.title