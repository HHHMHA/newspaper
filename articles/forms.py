from django import forms
from django.contrib.auth import get_user_model

from articles.models import Article, Comment


class ArticleCreationForm(forms.ModelForm):
    """A form that create an article by the current user"""
    class Meta:
        model = Article
        fields = ('title', 'body',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """Attach the current user as the article author"""
        article = super().save(commit=False)
        article.author = self.user
        if commit:
            article.save()
        return article


class CommentCreationForm(forms.ModelForm):
    """A form that create a comment by the current user for the selected article"""
    class Meta:
        model = Comment
        fields = ('article', 'comment')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """Attach the current user as the article author"""
        comment = super().save(commit=False)
        comment.author = self.user
        if commit:
            comment.save()
        return comment


class ArticleVoteForm(forms.ModelForm):
    """A form that set the article like status by the current user"""
    class Meta:
        model = Article
        fields = ()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """Attach the current user as the article author"""
        article = super().save(commit=False)
        article.likes.remove(self.user) if self.user_likes_article(article) else article.likes.add(self.user)
        if commit:
            article.save()
        return article

    def user_likes_article(self, article) -> bool:
        """:return True if the user who submitted the request currently likes the article (before the request)"""
        return article.likes.filter(pk=self.user.pk).exists()
