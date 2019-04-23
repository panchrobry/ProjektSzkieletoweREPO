from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.

def loginSite(request):
    return render(request, 'accounts/login.html')
