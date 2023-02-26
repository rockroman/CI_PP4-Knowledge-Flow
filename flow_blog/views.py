from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View)
from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class BlogPageView(ListView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'


@method_decorator(login_required, name='dispatch')
class BlogDetailView(UserPassesTestMixin, DetailView):

    model = BlogPost
    context_object_name = 'post'
    template_name = 'flow_blog/blog_details.html'
    slug_field = 'slug'
    form = CommentForm

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        if self.request.user:
            return redirect('protect_profile')

    def post(self, request, *args, **kwargs):
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

    model = BlogPost
    form_class = BlogForm
    template_name = 'flow_blog/add_blog.html'
    success_message = 'YOU ADDED A NEW BLOG'

    # extract the user so it can be passed into form
    def get_form_kwargs(self):
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
        return redirect('protect_profile')


# @method_decorator(login_required, name='dispatch')
# class UpdateBlogView(UserPassesTestMixin, UpdateView):
#     model = BlogPost
#     template_name = 'flow_blog/edit_blog.html'
#     form_class = BlogForm

#     def form_valid(self, form):
#         form.instance.creator == self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         if self.request.user.profile.role and self.request.user.profile.bio:
#             return self.request.user

#     def handle_no_permission(self):
#         return redirect('protect_profile')

@method_decorator(login_required, name='dispatch')
class UpdateBlogView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'flow_blog/edit_blog.html'
    form_class = BlogForm
    success_message = 'YOU UPDATED YOUR BLOG'

    def get_form_kwargs(self):
        kwargs = super(UpdateBlogView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # pass the 'user' in kwargs
        return kwargs

    def form_valid(self, form):
        form.instance.creator == self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        return redirect('protect_profile')


@login_required
def delete_blog(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.user == post.creator:
        post.delete()
        messages.success(request, 'BLOG-POST IS DELETED')
        return HttpResponseRedirect(reverse('blog_page'))
    else:
        messages.error(request, "CAN'T BLOG-POST(YOU ARE NOT CREATOR) ")
        return HttpResponseRedirect(reverse('blog_page'))


def delete_comment(request, comment_id):
    users_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.id == users_comment.author.id:
        users_comment.delete()
        messages.success(request, 'COMMENT IS DELETED')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "CAN'T DELETE COMMENT(YOU ARE NOT CREATOR) ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def update_comment(request, comment_id):
#     # users_comment = get_object_or_404(Comment, id=comment_id)
#     if request.user.id == users_comment.author.id:      
#         if request.method == 'POST':
#             users_comment = get_object_or_404(Comment, id=comment_id)
#             updatet_content = request.POST['content']
#             users_comment.content = updatet_content
#             users_comment.save()
#             messages.success(request, 'COMMENT IS UPDATED')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     else:
#         messages.error(request, "CAN'T UPDATE COMMENT(YOU ARE NOT CREATOR) ")
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm(instance=comment)

    if request.method == 'POST' and request.user.id == comment.author.id:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'COMMENT IS UPDATED')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "CAN'T UPDATE COMMENT(YOU ARE NOT CREATOR) ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
