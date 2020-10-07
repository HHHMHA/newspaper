from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .mixins import UserIsArticleAuthor
from .models import Article, Comment


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list'


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail'


class ArticleUpdateView(LoginRequiredMixin, UserIsArticleAuthor, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, UserIsArticleAuthor, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete'
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create'
    fields = ('title', 'body', )
    login_url = 'login'

    def form_valid(self, form):
        """Attach the user who submitted the request as the article creator and save the form."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ()
    login_url = 'login'

    def form_valid(self, form):
        """Create comment object from the form data and set the current user as the author"""
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.request.POST.get('article'))
        form.instance.comment = self.request.POST.get('comment')
        return super().form_valid(form)
