from django import urls
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('terminal/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('writers/', include('writers.urls'), name='writers'),
    path('orders', views.orders, name='orders'),
    path('orders/order_details/<int:order_id>/', views.order_details, name='order_details'),
    path('<int:order_details>/bid', views.bid, name='bid')

]
