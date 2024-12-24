from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username = username)
        print(username, password)
        if user:
            auth = authenticate(username=username, password=password)
            if auth is None:
                messages.error(request, "Invalid Password")
                return redirect('/')
            else:
                login(request, auth)
                return redirect('dashboard.html')

        else:
            messages.error(request, "Invalid username")
            return redirect('/')

    return render(request,"login.html")

def SignUp(request):
    return render(request, 'signup.html')

def Logout():
    pass