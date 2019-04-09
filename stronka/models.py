from django.db import models
from datetime import datetime


# Create your models here.

class Team(models.Model):
    ID = models.CharField(primary_key = True,max_length = 3)
    Name = models.CharField(max_length = 30)
    Register_Date = models.DateField(default = datetime.now(),blank = False)
    City = models.CharField(max_length = 50)
    Company = models.CharField(max_length = 100)


class User(models.Model):

    Username = models.CharField(max_length = 30)
    Forename = models.CharField(max_length = 50)
    Surname = models.CharField(max_length = 50)
    TeamID = models.ForeignKey(Team,on_delete=models.CASCADE)
    Email = models.EmailField(max_length = 50)
    TShirtSize = (
        ('S','SMALL'),
        ('M','MEDIUM'),
        ('L','LARGE'),
        ('XL','EXTRALARGE'),
        ('XXL','EXTRAEXTRALARGE'),
    )
