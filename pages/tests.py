from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse


class HomePageTestS(SimpleTestCase):
    def test_get_home_page_by_path(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)

    def test_get_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(200, response.status_code)

    def test_right_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'home.html')
