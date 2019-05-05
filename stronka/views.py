from django.shortcuts import render, HttpResponse, redirect
from .models import Robot,Category,Team
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm,RobotCreationForm,addTeamForm,SignUpForm
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth import login, authenticate,get_user_model

# Create your views here.
def registerUserOwn(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Forename = form.cleaned_data.get('forename')
            user.profile.Surname = form.cleaned_data.get('surname')
            user.profile.Email = form.cleaned_data.get('email')
            user.profile.Size = form.cleaned_data.get('size')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect('/account/home/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home(request):

    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/home/')
    else:
        form = UserCreationForm()
        args = {'form':form}
        return render(request,'accounts/reg_form.html',args)

def addRobot(request):
    if request.method == 'POST':
        form = RobotCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                category = form.cleaned_data['category']

            except Category.DoesNotExist:
                category = None

            robot = Robot.objects.create(
                Name = name,
                CategoryID = category,
            )
            return redirect('/account/home/')
    else:
        form = RobotCreationForm()
        args = {'form':form}
        return render(request,'accounts/addrobot.html',args)

def addTeam(request):
    if request.method == 'POST':
        form = addTeamForm(request.POST)
        if form.is_valid():
            loginUser = request.user
            name = form.cleaned_data['name']
            regDate = datetime.now()
            city = form.cleaned_data['city']
            company = form.cleaned_data['company']
            country = form.cleaned_data['country']
            team = Team.objects.create(
                Name = name,
                Register_Date = regDate,
                City = city,
                Company = company,
                Country = country,
            )
            loginUser.profile.TeamID = Team.objects.get(Name = name)
            loginUser.save()
            return redirect('/account/home/')
    else:
        form = addTeamForm()
        args = {'form':form}
        return render(request,'accounts/addteam.html',args)

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
