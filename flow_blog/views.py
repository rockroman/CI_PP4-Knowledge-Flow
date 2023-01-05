from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


# Create your views here.
class BlogPageView(generic.ListView):
    model = BlogPost
    template_name = 'blog.html'
