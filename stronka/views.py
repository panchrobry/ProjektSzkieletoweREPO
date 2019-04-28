from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.core.mail import send_mail
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} wyslal wiadomosc: \n \n {1}".format(
                sender_name,form.cleaned_data['message']
            )
            try:
                send_mail('test',message,sender_email,['karolek9.10@o2.pl'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Nie Poszlo')
            return HttpResponse('Poszlo')
    else:
        form = ContactForm()
    return render(request,'accounts/contact.html', {'form':form})
