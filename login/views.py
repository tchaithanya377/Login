from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import loginform, signupform
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        fm = loginform(request=request, data=request.POST)
        if fm.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/profile')
    else:
        fm = loginform()
    return render(request, 'login.html', {'form':fm})

def sign_up(request):
    if request.method == 'POST':
        fm = signupform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile')
    else:
        fm = signupform()
    return render(request, 'signup.html', {'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'home.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/')
