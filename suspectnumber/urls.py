# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('suspectnumber/', contactView, name='suspectnumber'),
    path('success/', successView, name='success'),
]