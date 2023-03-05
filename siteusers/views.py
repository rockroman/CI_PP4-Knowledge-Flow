from django.shortcuts import (
    render,
    redirect,
    get_object_or_404, HttpResponseRedirect
)
from django.views.generic import (
     CreateView, DetailView, UpdateView, TemplateView, DeleteView
)
from django.contrib.auth.models import User
from .models import Profile
from .forms import Profileform,  UpdateMentorRole, UpdateStudentRole
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class AppUserSetUpProfile(SuccessMessageMixin, generic.UpdateView):

    model = Profile
    form_class = Profileform
    template_name = 'create_profile.html'
    success_url = reverse_lazy('see_profile')
    success_message = 'YOUR PROFLE IS SET UP SUCCESSFULLY'

    def get_object(self, *args, **kwargs):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SeeProfilePageView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user_profile_page.html'

    def get_object(self, *args, **kwargs):
        return self.request.user


class EditProfilePageView(SuccessMessageMixin,
                          LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = Profileform
    template_name = 'profile_update.html'
    success_url = reverse_lazy('see_profile')
    success_message = 'PROFILE IS UPDATED'

    def get_object(self, *args, **kwargs):
        return self.request.user.profile


class DeleteAppUser(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'delete_profile.html'
    # template_name = 'delete_profile_modal.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.filter(user=request.user)
            profile.delete()

        request.user.is_active = False
        request.user.save()

        return HttpResponseRedirect(reverse_lazy('account_logout'))


def redirect_view(request):
    if request.user.profile.role and request.user.profile.first_name:
        return redirect('home')
    else:
        return redirect('protect_profile')


def SetProfileRole(request):
    profile = Profile.objects.get(user=request.user)
    student_form = UpdateStudentRole(instance=profile)
    mentor_form = UpdateMentorRole(instance=profile)
    if request.method == 'POST':
        if 'student' in request.POST:
            student_form = UpdateStudentRole(request.POST, instance=profile)
            if student_form.is_valid():
                student_form.save()
                return redirect('appuser_SetUp_profile')
        if 'mentor' in request.POST:
            mentor_form = UpdateMentorRole(request.POST, instance=profile)
            if mentor_form.is_valid():
                mentor_form.save()
                return redirect('appuser_SetUp_profile')

    context = {}
    context = {
        'student_form': student_form,
        'mentor_form': mentor_form,
    }

    return render(request, 'choose_role.html', context=context)


def protect_profile_view(request):
    if request.user.profile.role:
        return redirect('appuser_SetUp_profile')
    else:
        return redirect('set_role')


def list_of_mentors(request):

    mentors_list = Profile.objects.filter(role='Mentor').all()
    context = {
        'mentors_list': mentors_list
    }
    return context
