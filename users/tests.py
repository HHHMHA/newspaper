from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class SignUpTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def test_get_signup_page_by_path(self):
        response = self.client.get('/users/signup/')
        self.assertEquals(response.status_code, 200)

    def test_get_signup_page_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_right_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_user_model(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEquals(get_user_model().objects.count(), 1)
        self.assertEquals(get_user_model().objects.first().username, self.username)
        self.assertEquals(get_user_model().objects.first().email, self.email)

    def test_create_user_form(self):
        response = self.client.post(path=reverse('signup'), data={
            'username': 'newuser',
            'email': 'newuser@gmail.com',
            'age': 15,
            'password1': '12345678KillYourSelf',
            'password2': '12345678KillYourSelf'
        })
        self.assertEquals(response.status_code, 302)
        self.validate_user()

    def test_weak_password_rejection(self):
        response = self.client.post(path=reverse('signup'), data={
            'username': 'newuser',
            'email': 'newuser@gmail.com',
            'age': 15,
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'This password is too common.')
        self.assertEquals(get_user_model().objects.count(), 0)

    def test_same_username_rejection(self):
        self.client.post(path=reverse('signup'), data={
            'username': 'newuser',
            'email': 'newuser@gmail.com',
            'age': 15,
            'password1': '12345678KillYourSelf',
            'password2': '12345678KillYourSelf'
        })
        response = self.client.post(path=reverse('signup'), data={
            'username': 'newuser',
            'email': 'newuser2@gmail.com',
            'age': 15,
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'A user with that username already exists.')
        self.validate_user()

    def validate_user(self):
        self.assertEquals(get_user_model().objects.count(), 1)
        self.assertEquals(get_user_model().objects.first().username, self.username)
        self.assertEquals(get_user_model().objects.first().email, self.email)
        self.assertTrue(get_user_model().objects.first().check_password('12345678KillYourSelf'))
