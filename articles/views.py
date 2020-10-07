from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit'
    login_url = 'login'

    def test_func(self):
        return self.get_object().is_author(self.request.user)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete'
    login_url = 'login'

    def test_func(self):
        return self.get_object().is_author(self.request.user)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create'
    fields = ('title', 'body', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
