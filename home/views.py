from django.shortcuts import render, redirect
from django.views import generic 
from django.contrib.auth.models import User
from siteusers.models import Profile


# Create your views here.


# class HomeView(generic.TemplateView):
#     if user.profile.role is None:
#         template_name = 'create_profile.html'
#     else:
#         template_name = 'index.html'
        
    
#     return render(request, template_name)
   
 

def home(request):
    template_name = 'index.html'
        
    return render(request, template_name)

    
