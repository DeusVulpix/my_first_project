from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeletelView
)
app_name = 'article'

urlpatterns = [

    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeletelView.as_view(), name='article-delete')

]
