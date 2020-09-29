from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class SignUpTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def test_get_signup_page_by_path(self):
        response = self.client.get('/users/signup/')
        self.assertEquals(200, response.status_code)

    def test_get_signup_page_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(200, response.status_code)

    def test_right_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_user_model(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEquals(1, get_user_model().objects.count())
        self.assertEquals(self.username, get_user_model().objects.first().username)
        self.assertEquals(self.email, get_user_model().objects.first().email)
