from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from .models import Robot,Category
from django.contrib.auth import authenticate
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
