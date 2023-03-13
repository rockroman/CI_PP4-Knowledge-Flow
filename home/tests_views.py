from django.test import TestCase, Client
from django.urls import reverse, resolve
from siteusers.models import User
from .forms import ContactUsForm


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

    def tearDown(self):
        self.user.delete()

    def test_form_with_unauthenticated_user(self):
        self.client = Client()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        form = ContactUsForm(data={
           'name': 'rock',
           'email': 'test@user.com',
           'subject': 'test subject',
           'message': 'well done'
        })
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('home'), data={
           'name': 'rock',
           'email': 'test@user.com',
           'subject': 'test subject',
           'message': 'well done'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NEED TO BE LOGGED IN TO SEND MESSAGE')
