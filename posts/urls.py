# posts/urls.py
from django.urls import path
from . import views
from .views import PostsPageView


urlpatterns = [
    path('posts/', views.PostsPageView.as_view(), name='Post'),
]