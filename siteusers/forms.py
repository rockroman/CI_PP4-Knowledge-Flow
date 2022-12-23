# use widget=forms.CheckboxSelectMultiple() for mentor
# maybe widget=forms.RadioSelect() if only one should be selected but if later user needs to select one more think of way for this 
# widget to be transformed to checkbox
from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'role', 'bio']
        role = forms.MultipleChoiceField(
            choices=ROLE, widget=forms.CheckboxSelectMultiple())

    widgets = {
        'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
    }


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] 

