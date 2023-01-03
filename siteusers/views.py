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


class AppUserProfile(generic.CreateView):
	model = Profile
	form_class = Profileform
	template_name = 'create_profile.html'

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


class DeleteProfileView(LoginRequiredMixin, DeleteView):
	model = Profile
	template_name = 'delete_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self, *args, **kwargs):
		return self.request.user.profile



# class EditProfilePageView(UpdateView):
# 	model = Profile
# 	form_class = ProfileUpdateForm
# 	template_name = 'edit_profile.html'
# 	# fields = ['image', 'last_name', 'email', 'bio']
# 	success_url = reverse_lazy('user_profile_page.html')

# 	def get_context_data(self, *args, **kwargs):
# 		users = Profile.objects.all()
# 		context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
# 		app_user = get_object_or_404(Profile, id=self.kwargs['pk'])
# 		context['app_user'] = app_user
# 		return context
	# def get_object(self):
	# 	return self.request.user
	
	
# ------- end of used code































# Create your views here.
# class ProfileView(CreateView):
#     # template_name = 'profile.html'
#     # model = Profile
#     form_class = ProfileForm 
#     template_name = 'profile.html'
#     success_url = reverse_lazy('home')

#     def get_initial(self):
#         initial = super().get_initial()
#         initial['username'] = self.request.user.username
#         initial['email'] = self.request.user.email
#         return initial

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         user = User.objects.get(id=self.request.user.id)
#         # return super().form_valid(form)
#         user.save()
#         self.object = form.save()


# @login_required      
# def UserProfilePage(request):
# 	if request.method == 'POST':
# 		user_form = Userform(request.POST, instance=request.user)
# 		profile_form = Profileform(request.POST, request.FILES, instance=request.user.profile)
# 		if user_form.is_valid() and profile_form.is_valid():
# 			user_form.save()
# 			profile_form.save()
# 			return redirect('home') 

# 	else:
# 		user_form = Userform(instance=request.user)
# 		profile_form = Profileform(instance=request.user.profile)

# 	context = {
# 		'user_form': user_form,
# 		'profile_form': profile_form
# 	}
	
# 	return render(request, 'profile.html', context)