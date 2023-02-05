from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=50, required=True)
    phone = forms.CharField(max_length=20, required=False)
    company = forms.CharField(max_length=50, required=False)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea(), required=True)

  
