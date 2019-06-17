from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Team(models.Model):
    def unique_rand():
        while True:
            code = get_random_string(length = 6)
            if not Team.objects.filter(TeamCode=code).exists():
                return code

    Name = models.CharField(max_length = 30)
    Register_Date = models.DateField(default = datetime.now(),blank = False)
    City = models.CharField(max_length = 50)
    Company = models.CharField(max_length = 100)
    Country = CountryField(blank_label='Select Country',multiple=True,default = 'Poland')
    TeamCode = models.CharField(max_length = 6, unique = True, default = unique_rand)
    def __str__(self):
        return self.Name


class Category(models.Model):
    Description = models.CharField(max_length = 255)
    Type = models.IntegerField(default = 0)
    #0 -> bez
    #1 -> sumo
    #2 -> lf
    def __str__(self):
        return self.Description
groups = (
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),

        )
class Robot(models.Model):
    Type = models.IntegerField(default = 0)
    #0 -> bez
    #1 -> sumo
    #2 -> lf

    Name = models.CharField(max_length = 50)
    TeamID = models.ForeignKey(Team,on_delete=models.CASCADE,null = True)
    CategoryID = models.ForeignKey(
                                        Category,
                                        on_delete=models.CASCADE,
                    
                                        )
    Passed = models.BooleanField(default = False)
    Group = models.CharField( choices = groups, max_length = 2,blank = False,null = True)
    Points = models.IntegerField(default = 0    )
    def __str__(self):
        return self.Name
class Match(models.Model):
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE,limit_choices_to={'Type': 1})
    IDRobot1 = models.ForeignKey(Robot,on_delete = models.CASCADE, related_name='robot1')
    IDRobot2 = models.ForeignKey(Robot,on_delete = models.CASCADE, related_name='robot2')
    Result = models.CharField(max_length = 50)

    Group = models.CharField(choices = groups,  max_length = 2,blank = False,null = True)

class Race(models.Model):
    CategoryID = models.ForeignKey(Category,on_delete=models.CASCADE,limit_choices_to={'Type': 2})
    IDRobot = models.ForeignKey(Robot,on_delete = models.CASCADE, related_name='robot', limit_choices_to={
                                                                                        'Type': 2,
                                                                                        })
    Result = models.FloatField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
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
    IsJudge = models.BooleanField(default = False)
    def __str__(self):
        return self.Forename + " "+self.Surname
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
