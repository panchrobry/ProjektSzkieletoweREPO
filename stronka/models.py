from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator

# Create your models here.

class Team(models.Model):
    Name = models.CharField(max_length = 30)
    Register_Date = models.DateField(default = datetime.now(),blank = False)
    City = models.CharField(max_length = 50)
    Company = models.CharField(max_length = 100)
    Country = CountryField(blank_label='Select Country',multiple=True,default = 'Poland')

class User(models.Model):

    Username = models.CharField(max_length = 30)
    Forename = models.CharField(max_length = 50)
    Surname = models.CharField(max_length = 50)
    TeamID = models.ForeignKey(Team,on_delete=models.CASCADE,blank = True, null=True)
    Email = models.EmailField(max_length = 50)
    TShirtSize = (
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
    )
    Size = models.CharField(choices = TShirtSize, max_length = 4, default = 'M')
class Category(models.Model):
    Description = models.CharField(max_length = 255)
    MinAge = models.IntegerField(null = True)
    MaxAge = models.IntegerField(null = True)

class Robot(models.Model):
    Name = models.CharField(max_length = 50)
    TeamID = models.ForeignKey(Team,on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE)
    Passed = models.BooleanField(default = False)

class Judge(models.Model):
    Forename = models.CharField(max_length = 50)
    Surname = models.CharField(max_length = 50)
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE)
    TelNumber = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    Email = models.EmailField(max_length=50)
class Match(models.Model):
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE)
    IDRobot1 = models.ForeignKey(Robot,on_delete = models.CASCADE, related_name='robot1')
    IDRobot2 = models.ForeignKey(Robot,on_delete = models.CASCADE, related_name='robot2')
    IDJudge = models.ForeignKey(Judge,on_delete = models.CASCADE, blank = True, null = True)
    Result = models.CharField(max_length = 50)
