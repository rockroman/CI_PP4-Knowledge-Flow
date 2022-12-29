from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from siteusers.models import Profile


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     user = request.user
    #     profile = Profile.objects.all()
    #     if user.is_authenticated is None:
    #         return render(request, 'index.html')
    #     if user.is_authenticated:
    #         if user.profile:
    #             return render(request, 'index.html')
    #     else:
    #         return redirect('create_myprofile')



# def home(request):
#     return render(request, "../templates/index.html")
