"""knowledgeflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home_urls'),
    path('siteusers/', include('siteusers.urls'), name='siteusers_urls'),
    path('accounts/', include('allauth.urls'),),
    path('flow_blog/', include('flow_blog.urls'), name='flow_blog_urls'),
    path('categories/', include('categories.urls'), name='categories_urls'),
    
]
