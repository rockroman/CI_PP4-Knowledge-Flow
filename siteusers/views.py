from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy


# Create your views here.
class ProfieView(CreateView):
    # template_name = 'profile.html'
    # form_class = ProfileForm
    model = Profile
    template_name = 'profile_form.html'
    fields = ['image', 'first_name', 'last_name','role', 'bio']
