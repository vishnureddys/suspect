# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Please enter your email id" ,required=True)
    subject = forms.CharField(label="Please enter the suspect number" ,required=True)
    message = forms.CharField(label="Please add some additional comments" ,widget=forms.Textarea, required=True)