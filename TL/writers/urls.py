from django import urls
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.writers_base, name='writers_base'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]
