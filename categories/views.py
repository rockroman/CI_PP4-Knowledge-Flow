from django.shortcuts import render
from django.views.generic import ListView
from . models import LearningCategory
from flow_blog.models import BlogPost

# Create your views here.


class LearningCategoryListView(ListView):
    template_name = 'category.html'
    context_object_name = 'cat_list'
