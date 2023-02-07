from django.test import TestCase, Client, RequestFactory
from .models import Profile, User
from .forms import Profileform
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve, reverse_lazy
from home.views import home
from home import views
from .views import AppUserSetUpProfile, SeeProfilePageView, EditProfilePageView
from .forms import Profileform


# # Create your tests here.


class TestSiteusersModel(TestCase):

    @classmethod
    def setUp(self):
        # Create test user

        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='miki',
 

        )

    def test_is_profile_created(self):
        # profile created is empty except user.username  until updating
        user_profile = Profile.objects.filter().last()
        self.assertEquals(user_profile.user.username, 'MyTestUser')
        self.assertEquals(user_profile.first_name, 'miki')
        self.assertEquals(user_profile.bio, '')

    def test_profile_string_method_returning_username(self):
        user = User.objects.create(
            username='test_user_2',
            password='mypass799',
            email='test@user2.com',
            id='2',
        )
        user.save()
        user_profile = Profile.objects.get(user=user)
        self.assertEqual(str(user_profile), 'test_user_2')

    def test_get_absolute_url(self):
        client = Client()
        user = User.objects.create(
            username='test_user_2',
            password='mypass799',
            email='test@user2.com',
            id='2',
        )
        user.save()
        user_profile = Profile.objects.get(user=user)
        response = client.get(user_profile.get_absolute_url())
        self.assertEqual(response.status_code, 200)


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
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user.com',
            bio='my biography'

        )

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
        request = self.factory.post('create_profile/', {
            'first_name': 'Rock',
            'last_name': 'Roman',
            'email': 'test@user.com',
            'bio': 'my biography'

        })
        request.user = self.user
        view = AppUserSetUpProfile.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)


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

    def test_get_object_method(self):
        request = self.factory.get('edit_profile/')
        request.user = self.user
        response = EditProfilePageView.as_view()(request)
        self.assertEqual(response.status_code, 200)


def test_protect_profile_view(self):
    

   
   
    
    


