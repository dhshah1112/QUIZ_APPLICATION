from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        
        return  loggedin(request)
    else:
        return invalidlogin(request)

def loggedin(request):
    return render(request,'loggedin.html')

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')