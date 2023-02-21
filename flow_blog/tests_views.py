from django.test import TestCase, Client, RequestFactory
from siteusers.models import Profile, User
from .models import BlogPost, Comment
from .views import BlogDetailView, AddBlogView,delete_blog
from django.contrib.auth.models import AnonymousUser
from .forms import BlogForm, CommentForm


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
        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            id='22'
            
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

    # def test_post_method(self):
    #     post = BlogPost.objects.create(
    #         creator=self.user,
    #         title='my test post',
    #         id='12'            

    #     )
        # form = CommentForm(data={
        #     'author': self.user,
        #     'blogpost':post,
        #     'content': 'test post'
        # })
        # self.factory = RequestFactory()
        # request = self.factory.post('blog/blog/<int:pk>', data={
        #    'author': self.user,
        #     'blogpost':post,
        #     'content': 'test post' 

        # })
        # request.user = self.user
        # view = BlogDetailView.as_view()
        # response = view(request)
        # self.assertEqual(Comment.objects.filter(blogpost=post).count(),1)
        # self.assertTrue(form.is_valid())

    # def test_context_data(self):
    #     self.client = Client()
    #     post = BlogPost.objects.create(
    #         creator=self.user,
    #         title='my test post',
    #         id='12'            

    #     )
    #     form = CommentForm()
    #     comment = Comment.objects.create(
    #         blogpost=post,
    #         author=self.user,
    #         content='test content')
    #     response = self.client.get('blog/blog/<int:pk>')
    #     self.assertIn('TestUser11',response.context)


class TestAddBlogView(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testRock',
            password='mynewpass',
            email='test.rock@bo.com',
            id='11'

        )
        self.user.save()
        self.user.set_password('mynewpass')
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role=''

        )
        # self.user2 = User.objects.create(
        #     username='NewTester',
        #     password='test123',
        #     email='testing@bo.com',
        #     id='22'

        # )
        # self.user2.save()
        # self.user.set_password('test123')
        # self.user.save()

        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            id='31'
        )

    def test_get_from_kwargs(self):
        self.factory = RequestFactory()
        request = self.factory.get('')
        request.user = self.user
        view = AddBlogView()
        view.request = request
        # response = view(request)
        kwargs = view.get_form_kwargs()
        # self.assertEqual(response.status_code, 302)
        self.assertIn('user', kwargs)
        self.assertEqual(kwargs['user'], self.user)
    
    def test_if_user_didnt_set_profile_role(self):
        self.client.login(username='testRock', password='mynewpass')
        response = self.client.get('/flow_blog/')
        self.assertEqual(response.status_code, 200)
        # response = self.client.get('/flow_blog/blog/blog/31')
        response = self.client.get('/flow_blog/blog/add_blog/')
        self.assertEqual(response.status_code, 302)
        self.user_profile = Profile.objects.update(
            user=self.user,
            role='Student'
        )
        # response = self.client.get('/flow_blog/blog/blog/31')
        response = self.client.get('/flow_blog/blog/add_blog/')
        self.assertEqual(response.status_code, 200)

        



class TestDeleteBlog(TestCase):

    def setUp(self):
        self.client = Client()
        # Create test user
        self.user = User.objects.create(
            username='testRock',
            password='mynewpass',
            email='test.rock@bo.com',
            id='79'

        )
        self.user.save()
        # set password. Otherwise hash affects ability to log in.
        self.user.set_password('mynewpass')
        self.user.save()
        # updating user profile
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role='Student',
            id='10'

        )
        # create 2nd test user
        self.user2 = User.objects.create(
            username='miki',
            password='miki11',
            email='miki22@bo.com',
            id='44'
        )
        self.user2.save()
        # creating 1st test blog
        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            id='4',
            body='test body'
        )

    def test_view(self):
        # logging in and testing deletion of blog created by test user
        self.client.login(username='testRock', password='mynewpass')
        response = self.client.get('/flow_blog/delete_blog/4/')
        response = self.client.get('/flow_blog/', follow=True)
        self.assertEqual(BlogPost.objects.all().count(), 0)
        self.assertContains(response, 'BLOG-POST IS DELETED')
        # creating 2nd test blog
        post2 = BlogPost.objects.create(
            creator=self.user2,
            title='my new test',
            id='40',
            body='new test body'
        )
        # trying to delete blog that 1st test user didn't create
        response = self.client.get('/flow_blog/delete_blog/40/')
        self.assertRedirects(response, '/flow_blog/')
        response = self.client.get('/flow_blog/', follow=True)
        self.assertEqual(BlogPost.objects.all().count(), 1)
