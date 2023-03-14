"""
home views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from siteusers.models import User
from .forms import ContactUsForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHomeView(TestCase):

    def test_loading_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_load_right_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')


class TestContactFormSubmission(TestCase):
    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='NewTestUser',
            password='mypass7900',
            email='test@user.com',
            id='0',

        )
        self.user.save()
        self.user.set_password('mypass11')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_form_with_unauthenticated_user(self):
        self.client = Client()
        """
        navigating as anonymous user
        to a home page
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        form = ContactUsForm(data={
           'name': 'rock',
           'email': 'test@user.com',
           'subject': 'test subject',
           'message': 'well done'
        })
        self.assertTrue(form.is_valid())
        """
        anonymous user is filling out
        and submitting the form
        """
        response = self.client.post(reverse('home'), data={
           'name': 'rock',
           'email': 'test@user.com',
           'subject': 'test subject',
           'message': 'well done'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NEED TO BE LOGGED IN TO SEND MESSAGE')

    def test_form_with_logged_in_user(self):
        self.client = Client()
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('home'), data={
           'name': 'rock',
           'email': 'test@user.com',
           'subject': 'test subject',
           'message': 'well done'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'THANK YOU FOR YOUR MESSAGE')
