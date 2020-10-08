from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
from articles.models import Article, MAX_ROWS_FOR_ARTICLE


class ArticleModelTest(TestCase):
    title = 'Title'
    body = 'This is\nMy Body'
    date = datetime.now()
    
    def setUp(self) -> None:
        self.author = get_user_model().objects.create_user(
            username='j2mf',
            password='mysuperpass',
        )
        self.article = Article.objects.create(
            title=self.title,
            body=self.body,
            date=self.date,
            author=self.author
        )

    def test_create_article(self):
        self.assertEquals(Article.objects.count(), 1)
        actual_article = Article.objects.all()[0]
        self.assertEquals(actual_article.title, self.article.title)
        self.assertEquals(actual_article.body, self.article.body)
        self.assertEquals(actual_article.date, self.article.date)
        self.assertEquals(actual_article.author.pk, self.article.author.pk)

    def test_delete_article(self):
        self.article.delete()
        self.assertEquals(Article.objects.count(), 0)

    def test_change_article(self):
        self.article.title = 'I SEE YOU'
        self.article.save()
        self.assertEquals(Article.objects.first().title, self.article.title)

    def test_get_display_row_count(self):
        article = Article(
            title=self.title,
            body=self.body,
            date=self.date,
            author=self.author
        )
        self.assertEquals(article.get_display_rows_count(), 2)
        article.body = 'lots of lines \n\n\n\n\n\n\n\n hahaha'
        self.assertEquals(article.get_display_rows_count(), MAX_ROWS_FOR_ARTICLE)

# TODO Create rest of tests
# TODO create functional test with selinum
class ArticleViewTest(TestCase):
    pass
