from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper


# Create your views here.
class ProfileView(CreateView):
    # template_name = 'profile.html'
    # model = Profile
    form_class = ProfileForm 
    template_name = 'profile_form.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
       
        


    
