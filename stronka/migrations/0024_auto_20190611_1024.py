# Generated by Django 2.0.13 on 2019-06-11 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0023_auto_20190610_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 11, 10, 24, 0, 310871)),
        ),
    ]
