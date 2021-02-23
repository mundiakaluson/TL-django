from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bid, Order, Assign
from django.core.exceptions import ObjectDoesNotExist

title = "Tutoring Learners"

def home(request):
    return render(request, 'mainapp/home.html', {"title": title})

def about(request):
    return render(request, 'mainapp/about.html', {"title": title})

@login_required
def orders(request):
    #TODO: Render webpage to show orders after designing! DONE!
    orders = Order.objects.all()
    return render(request, 'mainapp/orders.html', {"title": title, "orders": orders})

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'mainapp/order_details.html', {'order': order})

def bid(request):
    
    if request.method == 'POST':
        if request.POST['order_id'] and request.POST['order_topic'] and request.POST['bid_note'] and request.POST['bidder']:
            bid = Bid()
            bid.order_id = request.POST['order_id']  
            bid.order_topic = request.POST['order_topic']
            bid.bid_note = request.POST['bid_note']
            bid.bidder = request.POST['bidder']
            bid.save()
            return render(request, 'mainapp/success.html')

    return render(request, 'mainapp/success.html')

    return render(request, 'mainapp/orders.html')

def assigned(request):
        writer_orders = Assign.objects
        return render(request, 'mainapp/assigned.html', {'writer_orders': writer_orders, 'orders': orders})   

def assigned_details(request, order_id):
    assigned_details = get_object_or_404(Order, pk=order_id)
    return render(request, 'mainapp/order_details.html', {'assigned_details': assigned_details})
