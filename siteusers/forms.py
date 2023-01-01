# use widget=forms.CheckboxSelectMultiple() for mentor
# maybe widget=forms.RadioSelect() if only one should be selected but if later user needs to select one more think of way for this 
# widget to be transformed to checkbox
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# ----used code
class Profileform(forms.ModelForm):
   
    role = forms.ChoiceField(widget=forms.RadioSelect(), choices=Profile.ROLE)
   
    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'email', 'role', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'CREATE PROFILE'))
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','first_name', 'last_name', 'role', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'update PROFILE'))

