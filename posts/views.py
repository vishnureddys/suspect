from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import ListView
from .models import Post


class PostsPageView(ListView):
    model = Post
    template_name = 'posts.html'