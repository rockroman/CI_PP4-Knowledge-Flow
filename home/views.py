"""
A module for home views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
# Internal:
from siteusers.models import Profile
from flow_blog.models import BlogPost
from .forms import ContactUsForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home(request):
    """
    view that renders homepage
    and contact form
    """
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            if request.user.is_authenticated:
                send_mail(
                        subject=name,
                        message=message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['2rock.rakic@gmail.com']
                    )
                messages.success(request, 'THANK YOU FOR YOUR MESSAGE')

                return redirect('.')
            else:
                messages.error(request, 'NEED TO BE LOGGED IN TO SEND MESSAGE')
                form = ContactUsForm()

    return render(request, 'index.html', {'form': form})
