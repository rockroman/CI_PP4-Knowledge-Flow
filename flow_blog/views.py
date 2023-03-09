"""
flow_blog view module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
# Internal:
from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm, UpdateCommentForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BlogPageView(ListView):
    """
    A class view to view a list off
    all blog posts
    """
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'


@method_decorator(login_required, name='dispatch')
class BlogDetailView(UserPassesTestMixin, DetailView):
    """
    Detail view for each blogpost
    and added comments
    """
    model = BlogPost
    context_object_name = 'post'
    template_name = 'flow_blog/blog_details.html'
    slug_field = 'slug'
    form = CommentForm

    def test_func(self):
        """
        testing if user has his profile role or profile set up
        correctly if not function fails
        """
        if self.request.user.profile.role and self.request.user.profile.bio:
            return True
        return False

    def handle_no_permission(self):
        """
        redirecting user to a propper view if profile role or bio
        is not set
        """
        if self.request.user:
            return redirect('protect_profile')

    def post(self, request, *args, **kwargs):
        """
        overriding the post method and
        savig the user comment
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            blogpost = self.get_object()
            form.instance.author = request.user
            form.instance.blogpost = blogpost
            form.save()
            messages.success(request, 'YOU ADDED A NEW COMMENT')
            return HttpResponseRedirect(
                reverse('blog_details', kwargs={'pk': blogpost.pk}))
        else:
            form = CommentForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get_context_data(self, **kwargs):
        """
        getting count of comments object
        and passing it into the context
        """
        post_comments_count = Comment.objects.all().filter(
            blogpost=self.object.id).count()
        post_comments = Comment.objects.all().filter(blogpost=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context


@method_decorator(login_required, name='dispatch')
class AddBlogView(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    """
    View for creating new blogposts
    """
    model = BlogPost
    form_class = BlogForm
    template_name = 'flow_blog/add_blog.html'
    success_message = 'YOU ADDED A NEW BLOG'

    def get_form_kwargs(self):
        """
        Extract the user from the
        kwargs so it can be passed into the form
        """
        kwargs = super(AddBlogView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # pass the 'user' in kwargs
        return kwargs

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        if self.request.user:
            return redirect('protect_profile')


class UpdateBlogView(UserPassesTestMixin, LoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):
    """
    Class View that updates blogposts
    """
    model = BlogPost
    template_name = 'flow_blog/edit_blog.html'
    form_class = BlogForm
    success_message = 'YOU UPDATED YOUR BLOG'

    def get_form_kwargs(self):
        """
        Extract the user from the
        kwargs so it can be passed into the form
        """
        kwargs = super(UpdateBlogView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # pass the 'user' in kwargs
        return kwargs

    def form_valid(self, form):
        form.instance.creator == self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


@login_required
def delete_blog(request, post_id):
    """
    View that handles deletion
    of the blogpost with supporting
    messages
    """
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.user == post.creator:
        post.delete()
        messages.success(request, 'BLOG-POST IS DELETED')
        return HttpResponseRedirect(reverse('blog_page'))
    else:
        messages.error(request, "CAN'T DELET BLOG-POST YOU ARE NOT CREATOR  ")
        return HttpResponseRedirect(reverse('blog_page'))


@login_required
def delete_comment(request, comment_id):
    """
    View that handles deletion
    of the comments with supporting
    messages
    """
    users_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.id == users_comment.author.id:
        users_comment.delete()
        messages.success(request, 'COMMENT IS DELETED')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "CAN'T DELETE COMMENT(YOU ARE NOT CREATOR) ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def list_of_comments(request):
    """
    view used as context processor
    so all comment object id's are available to all
    templates
    """
    context = {}
    context['comment_id'] = Comment.objects.first().id
    return context


class UpdateCommentView(LoginRequiredMixin, SuccessMessageMixin,
                        UserPassesTestMixin, UpdateView):
    """
    View that handles editing
    of a comment
    """
    model = Comment
    template_name = 'update_comment.html'
    form_class = CommentForm
    success_message = 'COMMENT IS UPDATED'

    def form_valid(self, form):
        form.instance.author.id == self.request.user.id
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
