from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Bid

title = "Tutoring Learners"

def home(request):
    return render(request, 'mainapp/home.html', {"title": title})

def about(request):
    return render(request, 'mainapp/about.html', {"title": title})

@login_required
def orders(request):
    #TODO: Render webpage to show orders after designing! DONE!
    orders = Order.objects

    if request.method == 'POST':
        order_bid = Order()
        order_bid.bid_placed_by = request.POST.get('bid_placed_by')
        order_bid.save()
        return render(request, 'mainapp/orders.html', {"title": title, "orders": orders})
    return render(request, 'mainapp/orders.html', {"title": title, "orders": orders})

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'mainapp/order_details.html', {'order': order})

def bid(request):

    if request.method == 'POST':

        if request.POST['bid_order'] and request.POST['bid_placed_by']:
            bid = Bid()
            bid.user_bid = request.user
            bid.bid_placed_by = request.POST['bid_placed_by']
            bid.save()
            return render(request, 'mainapp/success.html')

    return render(request, 'mainapp/success.html')
  