# Generated by Django 2.0.13 on 2019-05-01 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('stronka', '0005_auto_20190429_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 20, 6, 30, 367087)),
        ),
    ]
