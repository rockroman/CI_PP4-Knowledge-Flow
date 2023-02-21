from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from siteusers.models import Profile
from flow_blog.models import BlogPost
from .forms import ContactUsForm
from django.views.generic import TemplateView

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject=name,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['2rock.rakic@gmail.com']
            )
            messages.success(request, 'THANK YOU FOR YOUR MESSAGE')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ContactUsForm()

    return render(request, 'index.html', {'form': form})
