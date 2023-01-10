from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import BlogForm


# Create your views here.
class BlogPageView(ListView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'


class BlogDetailView(DetailView):

    model = BlogPost
    context_object_name = 'post'
    template_name = 'flow_blog/blog_details.html'


class AddBlogView(CreateView):

    model = BlogPost
    form_class = BlogForm
    template_name = 'flow_blog/add_blog.html'


class UpdateBlogView(UpdateView):
    model = BlogPost
    template_name = 'flow_blog/edit_blog.html'
    fields = ['title', 'body', 'cover_image']
