"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from posts import endpoints
from .views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    # path('api/', include(endpoints)),
    path( '', TemplateView.as_view(template_name='index.html')),
    path('posts/', views.post_list, name='post_list'),
    path('posts/new', views.post_form, name='post_form'),
    path('posts/<int:pk>', views.post_view, name="post_view"),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    #comments
    path('posts/comments/new', views.comment_create, name='comment_create'),
    path('comment/<int:pk>', views.comment_view, name="comment_view"),
    path('comment/edit/<int:pk>', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
