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

    orders = Order.objects
    order_check = Order.objects.filter(writer=request.user)
    return render(request, 'mainapp/orders.html', {"title": title, "orders": orders, "order_check": order_check})

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

    return render(request, 'mainapp/orders.html')

def assigned(request):
    try:
        orders = Order.objects
        if orders:
            return render(request, 'mainapp/assigned.html', {'orders': orders})   
    except ObjectDoesNotExist:
        return render(request, 'mainapp/assigned.html')

"""def assigned_details(request, order_id):
    assigned_details = get_object_or_404(Order, pk=order_id)

    return render(request, 'mainapp/assigned.html', {'assigned_details': assigned_details})"""

    

    