from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list'


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create'
    fields = ('title', 'body', 'author', )
