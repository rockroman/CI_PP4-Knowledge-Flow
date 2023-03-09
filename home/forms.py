"""
A module for home forms
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
# Internal:
from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 4}
    ), required=True)
