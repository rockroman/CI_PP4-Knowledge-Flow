from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import Profileform, ProfileUpdateForm
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class AppUserSetUpProfile(generic.UpdateView):

    model = Profile
    form_class = Profileform
    template_name = 'create_profile.html'
    success_url = reverse_lazy('see_profile')

    def get_object(self, *args, **kwargs):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)