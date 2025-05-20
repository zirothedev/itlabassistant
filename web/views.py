from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from web import models
from web.models import Itlab
from django.contrib.auth import authenticate, login
from calendar_app.views import Calendar
import datetime


# Create your views here.
def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method=='POST':
        Fullname=request.POST.get('Fullname')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        print(Fullname,Email,Password)
        my_user=User.objects.create_user(Fullname,Email,Password)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method=='POST':
        Fullname=request.POST.get('Fullname')
        Password=request.POST.get('Password')
        print(Fullname,Password)
        userr = authenticate(request, username=Fullname,password=Password)
        if userr is not None:
            login(request,userr)
            return redirect('base')
        else:
            return redirect('/login')
    return render(request, 'login.html')

def base(request):
    return render(request, 'base.html')

