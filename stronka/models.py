from django.db import models
from datetime import datetime


# Create your models here.

class Team(models.Model):
    ID = models.IntegerField(primary_key =  True)
    Name = models.CharField(max_length = 30)
    Register_Date = models.DateField(default = datetime.now(),blank = False)
    City = models.CharField(max_length = 50)

    Company = models.CharField(max_length = 100)
