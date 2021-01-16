from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writers_base, name='writers_base'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('<int:username>', views.username, name='username'),
    path('logout', views.logout, name='logout'),
]
