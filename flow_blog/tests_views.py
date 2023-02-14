from django.test import TestCase, Client, RequestFactory
from siteusers.models import Profile, User
from .models import BlogPost, Comment
from .views import BlogDetailView,AddBlogView
from django.contrib.auth.models import AnonymousUser
from .forms import BlogForm


class TestBlogDetailView(TestCase):
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create(
            username='TestUser11',
            password='mypass11',
            email='test@user11.com',
            id='11',
        )
        self.user.save()
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role='Student'

        )

    def test_test_function(self):
        
        self.factory = RequestFactory()
        request = self.factory.get('blog/blog/<int:pk>')
        request.user = self.user
        response = BlogDetailView.as_view()(request)
        view = BlogDetailView()
        view.request = request
        client = Client()
        
        self.client.force_login(self.user)
        self.assertEqual(response.status_code, 302)
      

class TestAddBlogView(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testRock',
            password='mynewpass',
            email='test.rock@bo.com',

        )
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role='Student'

        )        

        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test'
        )
    def test_get_from_kwargs(self):
        self.factory = RequestFactory()
        # request = self.factory.post('blog/add_blog/', {
        #     'title': 'Rocky new',
        #     'creator': self.user,
        #     'body': 'text of blog'
           

        # })
        request = self.factory.get('')
        request.user = self.user
        view = AddBlogView()
        view.request = request
        # response = view(request)
        kwargs = view.get_form_kwargs()
        # self.assertEqual(response.status_code, 302)
        self.assertIn('user', kwargs)
        self.assertEqual(kwargs['user'], self.user)
        
        
        
        
        


      




