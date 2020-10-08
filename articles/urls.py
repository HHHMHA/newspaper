from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    CommentCreateView,
    ArticleVoteView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('vote/<int:pk>', ArticleVoteView.as_view(), name='vote'),
]
