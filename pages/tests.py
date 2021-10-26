from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class PagesTestsViews(TestCase):
    # setup client
    def setup(self):
        self.client = Client()

    # testing home page
    def test_home_page(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    # testing about page
    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
