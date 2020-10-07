from tkinter import CASCADE

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from users.models import CustomUser

COMMENT_MAX_PEEK_LENGTH = 50
MAX_ROWS_FOR_ARTICLE = 5


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])

    def get_display_rows_count(self):
        """:return: A Limit for how many rows to display without scrolling for the article"""
        return min(MAX_ROWS_FOR_ARTICLE, len(self.body.split('\n')))


class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.limited_comment()

    def limited_comment(self):
        """
        Comment with limited length
        if the COMMENT_MAX_PEEK_LENGTH is exceeded the comment get cropped and 4 dots are appended to the comment
        """
        return self.comment[:COMMENT_MAX_PEEK_LENGTH] + self.tail()

    def tail(self):
        """:return 4 dots if the comment length exceeds the COMMENT_MAX_PEEK_LENGTH"""
        return "...." if len(self.comment) > COMMENT_MAX_PEEK_LENGTH else ""

    def get_absolute_url(self):
        return reverse('article_list')
