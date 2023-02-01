from django.test import TestCase
from django.urls import reverse, resolve


class TestHomeView(TestCase):

    def test_loading_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_load_right_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
