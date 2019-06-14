from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import *
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
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .filters import *

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

    robFilter = RobotsFilter(request.GET,queryset = robots)
    return render(request, 'accounts/robots.html',{'filter':robFilter})

@login_required(login_url='/account/login/')
def team(request):
    user = request.user
    friends = Profile.objects.all().filter(TeamID = user.profile.TeamID)
    return render(request, 'accounts/team.html',{'friends':friends})


def matches(request):
    matches = Match.objects.all()
    filterMatches = MatchesFilter(request.GET, queryset = matches)
    return render(request, 'accounts/matches.html',{'filter':filterMatches})

def races(request):
    races = Race.objects.all().order_by('Result')
    filterRaces = RacesFilter(request.GET, queryset = races)
    return render(request, 'accounts/races.html',{'filter':filterRaces})



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
def createMatchLegoSumo(request):
    if request.method == 'POST':
        form = MatchFormLegoSumo(request.POST)
        if form.is_valid():
            robot1 = form.cleaned_data.get('robot1')
            robot2 = form.cleaned_data.get('robot2')
            category = robot1.CategoryID
            group = robot1.Group
            result = form.cleaned_data.get('result')
            obj = Match.objects.create(CategoryID = category,
                                        IDRobot1 = robot1,
                                        IDRobot2 = robot2,
                                        Result = result,
                                        Group = group,
                                        )
            return render(request, 'accounts/createMatchLegoSumo.html', {'form': form})
    else:
        messages.error(request,"error")
        form = MatchFormLegoSumo()
    return render(request, 'accounts/createMatchLegoSumo.html', {'form': form})

@login_required(login_url='/account/login/')
def createMatchSumo(request):
    if request.method == 'POST':
        form = MatchFormSumo(request.POST)
        if form.is_valid():
            robot1 = form.cleaned_data.get('robot1')
            robot2 = form.cleaned_data.get('robot2')
            category = robot1.CategoryID
            group = robot1.Group
            result = form.cleaned_data.get('result')
            obj = Match.objects.create(CategoryID = category,
                                        IDRobot1 = robot1,
                                        IDRobot2 = robot2,
                                        Result = result,
                                        Group = group,
                                        )
            return render(request, 'accounts/createMatchSumo.html', {'form': form})
    else:
        messages.error(request,"error")
        form = MatchFormSumo()
    return render(request, 'accounts/createMatchSumo.html', {'form': form})

@login_required(login_url='/account/login/')
def createMatchMiniSumo(request):
    if request.method == 'POST':
        form = MatchFormMiniSumo(request.POST)
        if form.is_valid():
            robot1 = form.cleaned_data.get('robot1')
            robot2 = form.cleaned_data.get('robot2')
            category = robot1.CategoryID
            group = robot1.Group
            result = form.cleaned_data.get('result')
            obj = Match.objects.create(CategoryID = category,
                                        IDRobot1 = robot1,
                                        IDRobot2 = robot2,
                                        Result = result,
                                        Group = group,
                                        )
            return render(request, 'accounts/createMatchMiniSumo.html', {'form': form})
    else:
        messages.error(request,"error")
        form = MatchFormMiniSumo()
    return render(request, 'accounts/createMatchMiniSumo.html', {'form': form})

@login_required(login_url='/account/login/')
def createRaceLF(request):
    if request.method == 'POST':
        form = RaceFormLF(request.POST)
        if form.is_valid():
            robot = form.cleaned_data.get('robot')
            category = robot.CategoryID
            result = form.cleaned_data.get('result')
            obj = Race.objects.create(CategoryID = category,
                                        IDRobot = robot,
                                        Result = result)
            return render(request, 'accounts/addraceLF.html', {'form': form})
    else:

        messages.error(request,"error")
        form = RaceFormLF()
    return render(request, 'accounts/addraceLF.html', {'form': form})

@login_required(login_url='/account/login/')
def createRaceLegoLF(request):
    if request.method == 'POST':
        form = RaceFormLegoLF(request.POST)
        if form.is_valid():
            robot = form.cleaned_data.get('robot')
            category = robot.CategoryID
            result = form.cleaned_data.get('result')
            obj = Race.objects.create(CategoryID = category,
                                        IDRobot = robot,
                                        Result = result)
            return render(request, 'accounts/addraceLegoLF.html', {'form': form})
    else:

        messages.error(request,"error")
        form = RaceFormLegoLF()
    return render(request, 'accounts/addraceLegoLF.html', {'form': form})


@login_required(login_url='/account/login/')
def judgePanel(request):
    return render(request, 'accounts/judgePanel.html')


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

@login_required(login_url='/account/login/')
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
                Type = category.Type,
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
            send_mail('test',message,sender_email,['ka rolek9.10@o2.pl',])
            return HttpResponse("Wiadomosc wyslana")
    else:
        form = ContactForm()
    return render(request,'accounts/contact.html', {'form':form})
def AutoGroup(request):
    if request.method == 'POST':
        form = GroupAuto(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            count = 0
            for robot in Robot.objects.filter(CategoryID=category):
                if count < 4:
                    robot.Group = 'A'
                    robot.save()
                if count < 8 and count >= 4:
                    robot.Group = 'B'
                    robot.save()
                if count < 12 and count >= 8:
                    robot.Group = 'C'
                    robot.save()
                if count >= 12:
                    robot.Group = 'D'
                    robot.save()
                count= count +1

            return redirect('/account/home/')
    else:
        form = GroupAuto()
        args = {'form':form}
        return render(request,'accounts/groupAuto.html',args)

    return render(request, 'accounts/groupAuto.html',{'form':form})
def ManualGroup(request):
    if request.method == 'POST':
        form = ManualGroupForm(request.POST)
        if form.is_valid():
            robot = form.cleaned_data['robot']
            group = form.cleaned_data['group']
            robot.Group = group
            robot.save()

            return redirect('/account/home/')
    else:
        form = ManualGroupForm()
        args = {'form':form}
        return render(request,'accounts/manualGroup.html',args)

    return render(request, 'accounts/manualGroup.html',{'form':form})
