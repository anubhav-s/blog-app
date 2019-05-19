from django.urls import path
from . import views

"""
This file is used to define the URLs for listing the blogs, seeing the blog in detail, editing the blog
and creating a new blog.
"""
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('post/new/', views.blog_new, name='blog_new'),
    path('post/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
]
