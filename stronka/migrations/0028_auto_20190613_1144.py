# Generated by Django 2.0.13 on 2019-06-13 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0027_auto_20190613_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='Points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 13, 11, 44, 41, 822185)),
        ),
    ]
