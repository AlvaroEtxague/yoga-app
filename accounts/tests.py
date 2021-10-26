from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class AccountsTestsViews(TestCase):
    # setup client
    def setup(self):
        self.client = Client()

    # testing register page
    def test_register_page(self):
        response = self.client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    # testing login page
    def test_login_page(self):
        response = self.client.get(
            reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    # testing register page post redirect
    def test_register_page_details_POST(self):
        response = self.client.post(reverse('register'), {
            'first_name': "Alvaro",
            'last_name': "Blob",
            'username': "bobblob",
            'email': "bob@test.com",
            'password': "Newpass123@",
            'password2': "Newpass123@",
        })

        self.assertEquals(response.status_code, 302)
