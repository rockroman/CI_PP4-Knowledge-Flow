from django.shortcuts import render, redirect
from django.views import generic 
from django.contrib.auth.models import User
from siteusers.models import Profile
# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth.decorators import user_passes_test

# Create your views here.

class HomeView( generic.TemplateView):
    template_name = 'index.html'
   



    
