from django.contrib.auth.forms import UserCreationForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone = PhoneNumberField()
	class Meta:
		model = User
		fields = ['username', 'email', 'phone', 'password1', 'password2']
