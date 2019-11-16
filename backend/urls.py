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
from django.urls import path
from .views import index, Test
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('test', Test, name='test'),
    path('posts/', views.post_detail, name='post_list'),
    path('posts/new', views.post_form, name='post_form'),
    path('posts/<int:pk>', views.post_view, name="post_view"),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
]
