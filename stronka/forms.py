from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from .models import Robot,Category

class JoinForm(forms.Form):
    teamID = forms.CharField(max_length = 8)

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
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class RobotCreationForm(forms.Form):
    categories = (
    (1,'cos'),
    (2,'innecos'),
    )
    name = forms.CharField(max_length = 100)
    category = forms.ModelChoiceField(queryset = Category.objects.all())
class addTeamForm(forms.Form):
    name = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    country = CountryField(blank_label='(Select Country)',multiple=True,default = 'Poland').formfield()
