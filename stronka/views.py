from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def home(request):

    return render(request, 'accounts/home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/home/')
    else:
        form = UserCreationForm
        args = {'form':form}
        return render(request,'accounts/reg_form.html',args)
