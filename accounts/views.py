# accounts/views.py
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created. You are now able to login.')
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'accounts/register.html' , {'form' : form})