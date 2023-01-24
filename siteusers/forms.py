from django import forms
from .models import Profile
from django.contrib.auth.models import User
from categories.models import LearningCategory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class Profileform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['website_url'].required = False
        self.fields['linkedIn_url'].required = False
        self.helper.add_input(Submit('submit', 'SET PROFILE'))
        try:
            self.fields['email'].initial = self.instance.user.email
        except User.DoesNotExist:
            pass

    email = forms.EmailField(label="Primary email")
    category = forms.ModelMultipleChoiceField(
        queryset=LearningCategory.objects.all(), widget=forms.CheckboxSelectMultiple() )

    class Meta:
        model = Profile

        fields = [
            'image', 'first_name', 'last_name', 'email', 'category',
            'website_url', 'linkedIn_url', 'bio']
        labels = {
            'website_url': 'Website url (optional)',
            'linkedIn_url': 'LinkedIn url (optional)'
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


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image', 'first_name', 'last_name', 'email',  'bio']


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.add_input(Submit('submit', 'update PROFILE'))


class UpdateStudentRole(forms.ModelForm):
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
    role = forms.ChoiceField(choices=Profile.ROLE, widget=forms.HiddenInput())
    mentor = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Profile
        fields = ['role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.initial['role'] = 'Mentor'
