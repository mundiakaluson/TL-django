from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth

title = "Tutoring Learners"

def writers_base(request):
    return render(request, 'writers/writing.html', {'title': title})

def register(request):

    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'writers/register.html', {'error': 'Username is Taken!'})

            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'], 
                    email=request.POST['email'], first_name=request.POST['first_name'], 
                    last_name=request.POST['second_name'])

                user.is_active = False
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'writers/register.html', {'error': 'Passwords must match!'})

    else:
        return render(request, 'writers/register.html')

def inactive(request):
    return render(request, 'inactive.html')

def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        elif user is None:
            return render(request, 'writers/login.html', {'error':'Username or passowrd is incorrect!'})
        elif user.is_active == False:
            redirect('inactive')
    else:
        return render(request, 'writers/login.html', {'approval_error': 'Your Account is not yet Approved!'})

def username(request, username):
    username = get_object_or_404(User, pk=username)
    return render(request, 'writers/login.html', {'username': username})

def logout(request):
        auth.logout(request)
        return redirect('home')