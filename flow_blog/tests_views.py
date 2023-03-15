"""
flow_blog views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
# Internal:
from siteusers.models import Profile, User
from .models import BlogPost, Comment
from .views import BlogDetailView, AddBlogView, delete_blog, UpdateBlogView
from .forms import BlogForm, CommentForm
from categories.models import LearningCategory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBlogDetailView(TestCase):
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        self.cient = Client()
        # Create test user
        self.user = User.objects.create(
            username='TestUser11',
            password='mypass11',
            email='test@user11.com',
            id='11',
        )
        self.user.save()
        self.user.set_password('mypass11')
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='',
            role='Student'

        )

        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            id='22'

        )

    def tearDown(self):
        self.user.delete()
        self.post.delete()

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

    def test_is_user_profile_set_right(self):
        # logged in user didnt set profile right
        self.client.login(username='TestUser11', password='mypass11')
        response = self.client.get('/flow_blog/blog/blog/22')
        # user is redirected to setting his profile,
        # can't access the content
        self.assertEqual(response.status_code, 302)
        # user sets his profile right
        self.user_profile = Profile.objects.update(
            user=self.user,
            bio='my bio is set'

        )
        response = self.client.get('/flow_blog/blog/blog/22')
        # user can access the content
        self.assertEqual(response.status_code, 200)

    def test_posting_a_comment(self):
        self.client.login(username='TestUser11', password='mypass11')
        # user sets his profile right
        self.user_profile = Profile.objects.update(
            user=self.user,
            bio='my bio is set'

        )
        # # user navigates to blogpost and adds a comment
        response = self.client.post('/flow_blog/blog/blog/22', {
            'author': self.user,
            'blogpost': self.post,
            'content': 'new comment'
        })
        # # comment is added
        self.assertEqual(response.status_code, 302)
        # user tries to add comment without content
        response = self.client.post('/flow_blog/blog/blog/22', {
            'author': self.user,
            'blogpost': self.post,
            'content': ''
        })
        self.assertEqual(response.status_code, 302)
        # no new comments since there was no content of a comment
        self.assertEqual(Comment.objects.filter(author=self.user).count(), 1)


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

        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            id='31'
        )

    def tearDown(self):
        BlogPost.objects.filter(creator=self.user).delete()
        LearningCategory.objects.filter(maker=self.user).delete()
        self.user.delete()

    def test_get_from_kwargs(self):
        self.factory = RequestFactory()
        request = self.factory.get('')
        request.user = self.user
        view = AddBlogView()
        view.request = request
        kwargs = view.get_form_kwargs()
        self.assertIn('user', kwargs)
        self.assertEqual(kwargs['user'], self.user)

    def test_if_user_didnt_set_profile_role(self):
        self.client.login(username='testRock', password='mynewpass')
        response = self.client.get('/flow_blog/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/flow_blog/blog/add_blog/')
        self.assertEqual(response.status_code, 302)
        self.user_profile = Profile.objects.update(
            user=self.user,
            role='Student'
        )
        response = self.client.get('/flow_blog/blog/add_blog/')
        self.assertEqual(response.status_code, 200)

    def test_form_valid(self):
        self.client.login(username='testRock', password='mynewpass')
        profile = Profile.objects.get(user=self.user)
        category = LearningCategory.objects.create(
            name='test category', maker=self.user)
        profile.category.add(category)
        profile = Profile.objects.update(
            user=self.user,
            role='Student'
        )
        self.url = reverse('add_blog')
        self.data = {
            'title': 'Test Blog', 'body': 'This is a test blog.',
            'category': category.pk, 'id': '66',
            'creator': self.user.profile.id}
        response = self.client.post(self.url, data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BlogPost.objects.filter(title='Test Blog').exists())
        self.assertTrue(BlogPost.objects.all().count(), 2)


class TestUpdateBlogView(TestCase):
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

        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            body='my test blog',
            id='31'
        )

    def tearDown(self):
        BlogPost.objects.filter(creator=self.user).delete()
        LearningCategory.objects.filter(maker=self.user).delete()
        self.user.delete()

    def test_get_from_kwargs(self):
        self.factory = RequestFactory()
        request = self.factory.get('')
        request.user = self.user
        view = UpdateBlogView()
        view.request = request
        kwargs = view.get_form_kwargs()
        self.assertIn('user', kwargs)
        self.assertEqual(kwargs['user'], self.user)

    def test_updating_blog_with_profile_role(self):
        self.client.login(username='testRock', password='mynewpass')
        self.user_profile = Profile.objects.update(
            user=self.user,
            role='Student'
        )
        response = self.client.get('/flow_blog/blog/edit_blog/31')
        self.assertEqual(response.status_code, 200)

    def test_form_valid(self):
        self.client.login(username='testRock', password='mynewpass')
        profile = Profile.objects.get(user=self.user)
        category = LearningCategory.objects.create(
            name='test category', maker=self.user)
        profile.category.add(category)
        profile = Profile.objects.update(
            user=self.user,
            role='Student'
        )
        self.url = '/flow_blog/blog/edit_blog/31'
        self.data = {
            'title': 'Test Blog', 'body': 'This is a test blog.',
            'category': category.pk, 'creator': self.user.profile.id}
        response = self.client.post(self.url, data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BlogPost.objects.filter(title='Test Blog').exists())


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

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.post.delete()

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


class TestDeleteComment(TestCase):
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
        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test',
            body='new test body',
            id='31'
        )

    def tearDown(self):
        self.user.delete()
        self.post.delete()

    def test_comment_deletion(self):
        # creating test user
        self.user = User.objects.create_user(
            username='testuser', password='password')
        # creating test comment
        self.comment = Comment.objects.create(
            author=self.user,
            blogpost=self.post,
            id=31,
            content='Test comment',

        )
        # 2nd test user
        self.user2 = User.objects.create_user(
            username='2ndtestuser', password='password2')
        # 2nd test comment
        self.comment2 = Comment.objects.create(
            author=self.user2,
            blogpost=self.post,
            id=33,
            content='Testing comment',

        )
        # login as first test user
        self.client.force_login(self.user)
        #  first test useris deleting his coment
        response = self.client.post(reverse(
            'delete_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 302)
        # comment deleted
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())
        # first test user tries deletion of 2nd test users comment
        response = self.client.post(reverse(
            'delete_comment', kwargs={'comment_id': self.comment2.id}))
        # comment is not deleted
        self.assertTrue(Comment.objects.filter(pk=self.comment2.pk).exists())


class TestUpdateCommentView(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        # creating test user
        self.user = User.objects.create(
            username='newTester', password='new password'
        )
        self.user.save()
        """
         updating user profile
        """
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rocky',
            last_name='Romano',
            email='test@user15.com',
            bio='my biography is',
            role='Student',
            id='15'

        )
        """
         creating test post
        """
        self.post = BlogPost.objects.create(
            creator=self.user,
            title='my test title',
            body='new test body',
            id='35',

        )
        """
        creating 2nd test user
        """
        self.user2 = User.objects.create(
            username='rockTestuser', password='rockpass'
        )
        self.user2.save()

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.post.delete()

    def test_updating_comment(self):
        self.client.force_login(self.user)
        """
        creating test comment
        """
        self.comment = Comment.objects.create(
            author=self.user,
            blogpost=self.post,
            id=33,
            content='Test comment one',

        )
        """
        checking if comment is created
        """
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())
        response = self.client.get('/flow_blog/blog/blog/35', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.filter(pk=self.comment.pk).count(), 1)
        self.assertTrue(self.comment.content == 'Test comment one')
        """
        updating the comment
        """
        response = self.client.get('/flow_blog/update_comment/33/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/flow_blog/update_comment/33/', data={
            'content': 'changed comment'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'COMMENT IS UPDATED')
