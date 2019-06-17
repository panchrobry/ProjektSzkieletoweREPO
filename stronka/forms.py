from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from .models import *
from django.contrib.auth import authenticate
from django.db.models import Q
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
class JoinForm(forms.Form):
    teamID = forms.CharField(max_length = 8)
    result = Team.objects.filter(TeamCode = teamID).count()
    def clean(self):
        teamIDtemp = self.cleaned_data['teamID']
        teams = Team.objects.filter(TeamCode = teamIDtemp).count()
        if teams==0:
            raise forms.ValidationError("Taka drużyna nie istnieje")

class ChangeForm(UserChangeForm):
    forename = forms.CharField(max_length = 100,required = False)
    surname = forms.CharField(max_length = 100,required = False)

    class Meta:
        model = User

        fields = (
                'forename',
                'surname',
                'password',
                )
results = (
            ('Wygrał Robot1','Wygrał Robot1'),
            ('Remis','Remis'),
            ('Wygrał Robot2','Wygrał Robot2'),

        )
class MatchFormLegoSumo(forms.Form):
    robot1 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 2)), empty_label='None')
    robot2 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 2)), empty_label='None')
    result = forms.ChoiceField(choices = results)
    def clean(self):
        robot1 = self.cleaned_data['robot1']
        robot2 = self.cleaned_data['robot2']
        if robot1.CategoryID != robot2.CategoryID:
            raise forms.ValidationError("Nie ta sama kategoria")
        if robot1== robot2:
            raise forms.ValidationError("Nie moga byc te same roboty")

class MatchFormSumo(forms.Form):
    robot1 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 3)), empty_label='None')
    robot2 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 3)), empty_label='None')
    result = forms.ChoiceField(choices = results)
    def clean(self):
        robot1 = self.cleaned_data['robot1']
        robot2 = self.cleaned_data['robot2']
        if robot1.CategoryID != robot2.CategoryID:
            raise forms.ValidationError("Nie ta sama kategoria")
        if robot1== robot2:
            raise forms.ValidationError("Nie moga byc te same roboty")
class MatchFormMiniSumo(forms.Form):
    robot1 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 4)), empty_label='None')
    robot2 = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 4)), empty_label='None')
    result = forms.ChoiceField(choices = results)
    def clean(self):
        robot1 = self.cleaned_data['robot1']
        robot2 = self.cleaned_data['robot2']
        if robot1.CategoryID != robot2.CategoryID:
            raise forms.ValidationError("Nie ta sama kategoria")
        if robot1== robot2:
            raise forms.ValidationError("Nie moga byc te same roboty")
class RaceFormLF(forms.Form):
    robot = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 5)), empty_label='None')
    result = forms.FloatField(min_value = 0 )
class RaceFormLegoLF(forms.Form):
    robot = forms.ModelChoiceField(queryset = Robot.objects.filter(Q(CategoryID = 6)), empty_label='None')
    result = forms.FloatField(min_value = 0 )


class SignUpForm(UserCreationForm):
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(required=True)
    forename = forms.CharField(max_length = 100)
    surname = forms.CharField(max_length = 100)
    TShirtSize = (
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
    )
    size = forms.ChoiceField(choices = TShirtSize)
    class Meta:
        model = User
        fields = (
                    'username',
                    'email',
                    'forename',
                    'surname',
                    'size',
                    'password1',
                    'password2',

                    )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100,widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter your name'
            }
    ))
    email= forms.CharField(max_length=100,
                           widget= forms.EmailInput(
                            attrs={
                            'placeholder':'Enter your email'
                            }
                        ))
    message = forms.CharField(widget=forms.Textarea(
                        attrs={
                        'placeholder':'Enter your message'
                        }
    ))

class RobotCreationForm(forms.Form):
    name = forms.CharField(max_length = 100)
    category = forms.ModelChoiceField(queryset = Category.objects.all())
class addTeamForm(forms.Form):
    name = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    country = CountryField(blank_label='(Select Country)',multiple=True,default = 'Poland').formfield()
class GroupAuto(forms.Form):
    category = forms.ModelChoiceField(queryset = Category.objects.all())
class ManualGroupFormLS(forms.Form):
    groups = (
                ('A','A'),
                ('B','B'),
                ('C','C'),
                ('D','D'),

            )
    robot = forms.ModelChoiceField(queryset = Robot.objects.filter(CategoryID = 2))
    group = forms.ChoiceField(choices = groups)
class ManualGroupFormMS(forms.Form):
    groups = (
                ('A','A'),
                ('B','B'),
                ('C','C'),
                ('D','D'),

            )
    robot = forms.ModelChoiceField(queryset = Robot.objects.filter(CategoryID = 4))
    group = forms.ChoiceField(choices = groups)
class ManualGroupFormS(forms.Form):
    groups = (
                ('A','A'),
                ('B','B'),
                ('C','C'),
                ('D','D'),

            )
    robot = forms.ModelChoiceField(queryset = Robot.objects.filter(CategoryID = 3))
    group = forms.ChoiceField(choices = groups)
