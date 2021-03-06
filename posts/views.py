from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import ListView
from .models import Post


class PostsPageView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'