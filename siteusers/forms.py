"""
A module for views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# Internal:
from .models import Profile
from categories.models import LearningCategory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profileform(forms.ModelForm):
    """
    A class view for creating
    and updating user profile
    """

    def __init__(self, *args, **kwargs):
        """
        overriding init method and setting
        email field as user object field
        """
        super(Profileform, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['website_url'].required = False
        self.fields['linkedIn_url'].required = False
        self.helper.add_input(Submit('submit', 'SET PROFILE'))
        self.fields['email'].initial = self.instance.user.email

    email = forms.EmailField(label="Primary email")
    category = forms.ModelMultipleChoiceField(
        queryset=LearningCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple())
    website_url = forms.URLField(max_length=60)
    linkedIn_url = forms.URLField(max_length=50)

    class Meta:
        model = Profile

        fields = [
            'image', 'first_name', 'last_name', 'email', 'category',
            'website_url', 'linkedIn_url', 'bio']
        labels = {
            'website_url': 'Website url (optional)',
            'linkedIn_url': 'LinkedIn url (optional)',


        }

    def save(self, *args, **kwargs):
        """
        Update the primary email address on the related User object as well.
        """
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(Profileform, self).save(*args, **kwargs)
        return profile


class UpdateStudentRole(forms.ModelForm):
    """
    A class view for updating
    profile role as a student
    """
    role = forms.ChoiceField(choices=Profile.ROLE, widget=forms.HiddenInput())
    student = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Profile
        fields = ['role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.initial['role'] = 'Student'


class UpdateMentorRole(forms.ModelForm):
    """
    A class view for updating
    profile role as a mentor
    """
    role = forms.ChoiceField(choices=Profile.ROLE, widget=forms.HiddenInput())
    mentor = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Profile
        fields = ['role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.initial['role'] = 'Mentor'
