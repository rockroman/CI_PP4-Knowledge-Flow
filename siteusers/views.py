from django.shortcuts import render
from django.views.generic.list import View
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
class SiteUserProfieView(View):
    model = Profile
