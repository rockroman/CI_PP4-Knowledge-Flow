from django.test import TestCase, Client, RequestFactory
from .models import Profile, User
from .forms import Profileform
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve, reverse_lazy
from home.views import home
from home import views
from .views import AppUserSetUpProfile, SeeProfilePageView, EditProfilePageView, protect_profile_view
from .forms import Profileform
from django.http import HttpRequest
from http import HTTPStatus


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


class TestProtectProfileView(TestCase):
    # self.factory = RequestFactory()
    # Create test user
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
            bio='my biography',
            role='Student'

        )
        


    def test_protect_profile(self):
        request = self.factory.get('protect_profile/')
        request.user = self.user
        response = protect_profile_view(request)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed('profile_update.html')
    
    # def test_protect_profile2(self):
    #     request = self.factory.get('protect_profile/')
    #     request.user = self.user
    #     request.profile = Profile.objects.update(
    #         user=self.user,
    #         first_name='Rock2',
    #         last_name='Roman2',
    #         email='test@user2.com',
    #         bio='my biography',
    #         role='Student'

    #     )
        
    #     response = protect_profile_view(request)
    #     # self.assertEqual(response.status_code, 302)
    #     self.assertEqual(request.user.profile.role, "Student")

    # ------------- testing Forms


# class TestProfileForm(TestCase):
#     def setUp(self):
#         self.url = reverse_lazy('see_profile')
#         self.user = User.objects.create(username='Mike',email='mike@bo.com')

#     def test_profile_update_page_exists(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 302)
        
#     def test_is_user_email_updated(self):
#         form = Profileform(instance=self.user, data={
#             'email': 'newmail@net.com'
#         })
#         self.assertTrue(form.is_valid())
