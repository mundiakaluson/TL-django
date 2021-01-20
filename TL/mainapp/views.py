from django.shortcuts import render
from django.contrib.auth.decorators import login_required

title = "Tutoring Learners"

def home(request):
    return render(request, 'mainapp/home.html', {"title": title})

def about(request):
    return render(request, 'mainapp/about.html', {"title": title})

@login_required
def orders(reqeust):
    return render(reqeust, 'mainapp/orders.html', {"title": title})