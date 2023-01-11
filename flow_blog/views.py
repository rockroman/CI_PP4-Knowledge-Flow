from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.first_name:
            return self.request.user

    def handle_no_permission(self):
        if self.request.user:
            return redirect('protect_profile')


class AddBlogView(LoginRequiredMixin, CreateView):

    model = BlogPost
    form_class = BlogForm
    template_name = 'flow_blog/add_blog.html'


class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'flow_blog/edit_blog.html'
    form_class = BlogForm


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/delete_blog.html'
    success_url = reverse_lazy('blog_page')
