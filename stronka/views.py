from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.

def loginSite(request):
    dane = ['Michał','to','cwel']
    name = 'Karol Nadolny'

    args = {'name': name, 'dane': dane}
    return render(request, 'accounts/login.html',args)

def home(request):
    dane = ['Michał','to','cwel']
    name = 'Karol Nadolny'

    args = {'name': name, 'dane': dane}
    return render(request, 'accounts/home.html',args)
