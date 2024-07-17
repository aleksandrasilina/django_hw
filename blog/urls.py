from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('', ArticleListView.as_view(), name='articles_list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]
