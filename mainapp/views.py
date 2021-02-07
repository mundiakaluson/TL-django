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
<<<<<<< HEAD:mainapp/views.py
    order_check = Order.objects.filter(writer=request.user)
    return render(request, 'mainapp/orders.html', {"title": title, "orders": orders, "order_check": order_check})
=======
<<<<<<< HEAD
=======

    if request.method == 'POST':
        order_bid = Order()
        order_bid.bid_placed_by = request.POST.get('bid_placed_by')
        order_bid.save()
        return render(request, 'mainapp/orders.html', {"title": title, "orders": orders})
>>>>>>> 1ba393cb26e33683f0aeaca01e79c4ed4c2ee48c
    return render(request, 'mainapp/orders.html', {"title": title, "orders": orders})
>>>>>>> origin/main:TL/mainapp/views.py

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'mainapp/order_details.html', {'order': order})

def bid(request):
    
    if request.method == 'POST':
<<<<<<< HEAD
        if request.POST['order_id'] and request.POST['order_topic'] and request.POST['bid_note'] and request.POST['bidder']:
            bid = Bid()
            bid.order_id = request.POST['order_id']  
            bid.order_topic = request.POST['order_topic']
            bid.bid_note = request.POST['bid_note']
            bid.bidder = request.POST['bidder']
            bid.save()
            return render(request, 'mainapp/success.html')

    return render(request, 'mainapp/orders.html')

<<<<<<< HEAD:mainapp/views.py
def assigned(request):
        writer_orders = Assign.objects
        return render(request, 'mainapp/assigned.html', {'writer_orders': writer_orders, 'orders': orders})   

def assigned_details(request, order_id):
    assigned_details = get_object_or_404(Order, pk=order_id)
    return render(request, 'mainapp/order_details.html', {'assigned_details': assigned_details})
=======
    
=======

        if request.POST['bid_order'] and request.POST['bid_placed_by']:
            bid = Bid()
            bid.user_bid = request.user
            bid.bid_placed_by = request.POST['bid_placed_by']
            bid.save()
            return render(request, 'mainapp/success.html')

    return render(request, 'mainapp/success.html')
  
>>>>>>> 1ba393cb26e33683f0aeaca01e79c4ed4c2ee48c
>>>>>>> origin/main:TL/mainapp/views.py
