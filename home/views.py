from django.shortcuts import render
from django.views import generic


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'index.html'

# def home(request):
#     return render(request, "../templates/index.html")
