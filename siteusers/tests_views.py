"""
siteusers views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client, RequestFactory
from django.http import HttpRequest
from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve, reverse_lazy
from home.views import home
from home import views
# Internal:
from .models import Profile, User
from .views import (AppUserSetUpProfile,
                    SeeProfilePageView, EditProfilePageView,
                    protect_profile_view)
from .forms import Profileform
from categories.models import LearningCategory
from home.views import home
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestAppUserSetUpProfile(TestCase):
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create(
            username='NewTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()
        self.user.set_password('mypass79')
        self.user.save()
        #  update existing profile
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user.com',
            bio='my biography'

        )

    def tearDown(self):
        self.user.delete()

    def test_success_url(self):
        client = Client()
        response = client.get(reverse_lazy('see_profile'))
        self.assertEqual(response.status_code, 302)

    def test_get_object_method(self):
        request = self.factory.get('create_profile/')
        request.user = self.user
        response = AppUserSetUpProfile.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_is_the_form_valid(self):
        self.client = Client()
        # creating new test user
        user2 = User.objects.create(
            username='Tester22',
            password='testpass',
            id=88
        )
        user2.save()
        user2.set_password('testpass')
        user2.save()
        self.assertTrue(Profile.objects.filter(user=user2).exists())
        self.client.login(username='Tester22', password='testpass')
        profile = Profile.objects.get(user=user2)
        # updating new test user profile
        profile = Profile.objects.update(
            role='Mentor'
        )
        self.assertTrue(Profile.objects.filter(role='Mentor').exists())
        self.category = LearningCategory.objects.create(
            name='test category', maker=user2, id=22)
        response = self.client.get('/siteusers/create_profile/')
        self.assertEqual(response.status_code, 200)
        # creating the profile
        response = self.client.post('/siteusers/create_profile/', data={
            'first_name': 'Mike',
            'last_name': 'tester',
            'email': 'test@user.com',
            'category': self.category.pk,
            'bio': 'my biography',
            'id': '76'

        }, follow=True)
        self.assertEqual(response.status_code, 200)
        # checking is the profile created
        self.assertTrue(Profile.objects.filter(
            category=self.category.pk).exists())
        self.assertContains(response, 'YOUR PROFLE IS SET UP SUCCESSFULLY')


class TestProfilePageView(TestCase):
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create(
            username='NewTestUser3',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock'

        )

    def tearDown(self):
        self.user.delete()

    def test_details(self):
        request = self.factory.get('see_profile/')
        request.user = self.user
        response = SeeProfilePageView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestEditProfilePageView(TestCase):

    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create(
            username='NewTestUser2',
            password='mypass799',
            email='test@user2.com',
            id='1',
        )
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock2',
            last_name='Roman2',
            email='test@user2.com',
            bio='my biography'

        )

    def tearDown(self):
        self.user.delete()

    def test_get_object_method(self):
        request = self.factory.get('edit_profile/')
        request.user = self.user
        response = EditProfilePageView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestProtectProfileView(TestCase):
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create(
            username='NewTestUser2',
            password='mypass799',
            email='test@user2.com',
            id='1',
        )
        self.user.save()
        self.user.set_password('mypass799')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_protect_profile(self):
        self.client = Client()
        self.client.login(username='NewTestUser2', password='mypass799')
        # attempt to get view without setting profile role
        response = self.client.get('/siteusers/protect_profile/')
        self.assertEqual(response.status_code, 302)
        # user redirected to set profile role
        self.assertRedirects(response, '/siteusers/set_role/')
        # user sets only profile role
        self.user_profile = Profile.objects.update(
            user=self.user,
            role='Student'

        )
        response = self.client.get('/siteusers/protect_profile/')
        # user gets redirected to create full profile
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/siteusers/create_profile/')


class TestRedirectView(TestCase):
    @classmethod
    def setUp(self):
        # Create test user
        self.client = Client()
        self.user = User.objects.create(
            username='NewTestUser2',
            password='mypass799',
            email='test@user2.com',
            id='1',
        )
        self.user.save()
        self.profile = Profile.objects.update(
            user=self.user,
            role='Mentor'

        )

    def test_user_with_set_role(self):
        self.client.login(username='NewTestUser2', password='mypass799')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/flow_blog/blog/add_blog/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('create_profile.html')
