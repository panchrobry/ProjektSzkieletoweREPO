# Generated by Django 2.0.13 on 2019-04-24 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0015_auto_20190423_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 0, 46, 52, 490604)),
        ),
    ]
