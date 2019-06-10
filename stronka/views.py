from django.shortcuts import render, HttpResponse, redirect
from .models import Robot,Category,Team, Match, Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import (ContactForm,
                    RobotCreationForm,
                    addTeamForm,
                    SignUpForm,
                    JoinForm,
                    ChangeForm,
                    LoginForm,
                    MatchForm,
                    )
from django.contrib.auth import logout
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth import (
                                login,
                                authenticate,
                                get_user_model,
                                update_session_auth_hash,

                                )
from django.shortcuts import render_to_response
import os

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('/account/home/')
        return render(request, 'accounts/login.html', {'form': form })
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form })

def view_robots(request):
    robots = Robot.objects.all()
    return render(request, 'accounts/robots.html',{'robots':robots})

@login_required(login_url='/account/login/')
def team(request):
    user = request.user
    friends = Profile.objects.all().filter(TeamID = user.profile.TeamID)
    return render(request, 'accounts/team.html',{'friends':friends})


def matches(request):
    matches = Match.objects.all()
    return render(request, 'accounts/matches.html',{'matches':matches})


@login_required(login_url='/account/login/')
def export(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    p = canvas.Canvas(response)
    x= 800
    user = request.user
    friends = Profile.objects.filter(TeamID = user.profile.TeamID)
    druzyna = user.profile.TeamID.Name + " w skladzie:"

    p.drawString(50, x, druzyna)
    x= x-12
    for friend in friends:
        p.drawString(50, x, friend.Forename+" "+friend.Surname)
        x= x-12
    p.drawString(50, x, "Uczestniczyla w zawodach EastROBO2019")
    p.showPage()
    p.save()
    return response

@login_required(login_url='/account/login/')
def createMatch(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            user = request.user
            robot1 = form.cleaned_data.get('robot1')
            robot2 = form.cleaned_data.get('robot2')
            category = robot1.CategoryID
            judge = User.objects.get(id  = user.id)
            result = form.cleaned_data.get('result')
            obj = Match.objects.create(CategoryID = category,
                                        IDRobot1 = robot1,
                                        IDRobot2 = robot2,
                                        Result = result)
            return redirect('/account/home/')
    else:
        form = MatchForm()
    return render(request, 'accounts/fights.html', {'form': form})

@login_required(login_url='/account/login/')
def joinTeam(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            user = request.user
            user.profile.TeamID = Team.objects.get(TeamCode = form.cleaned_data.get('teamID'))
            user.save()
            return redirect('/account/home/')

    else:
        form = JoinForm()
        return render(request, 'accounts/jointeam.html', {'form': form})


@login_required(login_url='/account/login/')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Zmieniono hasło")
            return redirect('/account/home/')
        else:
            messages.error(request,"Popraw błąd")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changePassword.html',{'form': form})


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
            login(request, user)
            return redirect('/account/home/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home(request):

    return render(request, 'accounts/home.html')


@login_required(login_url='/account/login/')
def change(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            user = request.user
            forename = form.cleaned_data['forename']
            surname = form.cleaned_data['surname']
            if forename :

                user.profile.Forename = forename
            if surname:

                user.profile.Surname = surname

            user.save()
            return redirect('/account/home/')
    else:
        form = ChangeForm()
        args = {'form':form}
        return render(request,'accounts/change.html',args)






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


@login_required(login_url='/account/login/')
def addRobot(request):
    if request.method == 'POST':
        form = RobotCreationForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            try:
                category = form.cleaned_data['category']

            except Category.DoesNotExist:
                category = None

            robot = Robot.objects.create(
                Name = name,
                CategoryID = category,
                TeamID = user.profile.TeamID
            )
            return redirect('/account/home/')
    else:
        form = RobotCreationForm()
        args = {'form':form}
        return render(request,'accounts/addrobot.html',args)


@login_required(login_url='/account/login/')
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



def logout_view(request):
    logout(request)
    return HttpResponse("Wylogowano")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            messageForm = form.cleaned_data['message']
            message = sender_name +" " + sender_email+ " wyslal wiadomosc: " + messageForm
            send_mail('test',message,sender_email,['karolek9.10@o2.pl',])
            return HttpResponse("Wiadomosc wyslana")
    else:
        form = ContactForm()
    return render(request,'accounts/contact.html', {'form':form})
