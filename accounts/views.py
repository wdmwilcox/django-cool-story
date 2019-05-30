from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password_1'] == request.POST['password_2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User name has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password_1'])
                auth.login(request, user)
                return redirect('index.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password does not exist'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/logout.html')
