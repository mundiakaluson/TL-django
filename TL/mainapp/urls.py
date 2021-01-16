from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
]