from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 3
    extra_context = {
        'title': 'Блог'
    }


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:articles_list')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles_list')
