from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

title = "Tutoring Learners"

def home(request):
    return render(request, 'mainapp/home.html', {"title": title})

def about(request):
    return render(request, 'mainapp/about.html', {"title": title})

@login_required
def orders(reqeust):
    #TODO: Render webpage to show orders after designing!

    orders = Order.objects
    

    return render(reqeust, 'mainapp/orders.html', {"title": title, "orders": orders})
    
    