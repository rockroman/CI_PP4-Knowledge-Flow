"""
knowledgeflow views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client, RequestFactory
from django.http import HttpResponseServerError
from django.urls import reverse
from knowledgeflow import urls
# Internal:
from .views import handler500, handler403
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHandlerViews(TestCase):
    def test_500_error(self):
        factory = RequestFactory()
        request = factory.get('/')
        response = handler500(request)
        self.assertEqual(response.status_code, 500)

    def test_403_error(self):
        factory = RequestFactory()
        request = factory.get('/')
