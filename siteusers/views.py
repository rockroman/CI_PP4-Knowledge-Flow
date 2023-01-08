from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import Profileform, ProfileUpdateForm, UpdateStudentRole
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.core.exceptions import ObjectDoesNotExist



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

	


class SeeProfilePageView(LoginRequiredMixin, DetailView):
	model = Profile
	# form_class = Profileform
	template_name = 'user_profile_page.html'

	def get_object(self, *args, **kwargs):
		return self.request.user



class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
	model = Profile
	form_class = ProfileUpdateForm
	template_name = 'profile_update.html'
	success_url = reverse_lazy('see_profile')

	def get_object(self, *args, **kwargs):
		return self.request.user.profile


# class DeleteProfileView(LoginRequiredMixin, DeleteView):
# 	model = Profile
# 	template_name = 'delete_profile.html'
# 	success_url = reverse_lazy('home')

# 	def get_object(self, *args, **kwargs):
# 		return self.request.user.profile


def redirect_view(request):
	if request.user.profile.role:
		return redirect('home')
	else:
		return redirect('appuser_SetUp_profile')
	


class DeleteAppUser(LoginRequiredMixin, generic.DeleteView):
	model = User
	template_name = 'delete_profile.html'
	# success_url = reverse_lazy('accounts/logout')

	def get_object(self, *args, **kwargs):
		return self.request.user
	
	def post(self, request, *args, **kwargs):
		if Profile.objects.filter(user=request.user).exists():
			profile = Profile.objects.filter(user=request.user)
			profile.delete()
		
		request.user.is_active = False
		request.user.save()

		return HttpResponseRedirect(reverse_lazy('account_logout'))


# old new code
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


class SeeProfilePageView(LoginRequiredMixin, DetailView):
	model = Profile
	template_name = 'user_profile_page.html'

	def get_object(self, *args, **kwargs):
		return self.request.user


class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
	model = Profile
	form_class = ProfileUpdateForm
	template_name = 'profile_update.html'
	success_url = reverse_lazy('see_profile')

	def get_object(self, *args, **kwargs):
		return self.request.user.profile

def redirect_view(request):
	if request.user.profile.role:
		return redirect('home')
	else:
		return redirect('appuser_SetUp_profile')
	


class DeleteAppUser(LoginRequiredMixin, generic.DeleteView):
	model = User
	template_name = 'delete_profile.html'

	def get_object(self, *args, **kwargs):
		return self.request.user
	
	def post(self, request, *args, **kwargs):
		if Profile.objects.filter(user=request.user).exists():
			profile = Profile.objects.filter(user=request.user)
			profile.delete()
		
		request.user.is_active = False
		request.user.save()

		return HttpResponseRedirect(reverse_lazy('account_logout'))

class SetProfileRole(UpdateView):
	model = Profile
	form_class = UpdateStudentRole
	template_name = 'choose_role.html'
	success_url = reverse_lazy('appuser_SetUp_profile')
	

	def get_object(self):
		return self.request.user.profile

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
			

			
		 
