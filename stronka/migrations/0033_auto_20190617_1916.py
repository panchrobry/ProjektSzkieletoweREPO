# Generated by Django 2.0.13 on 2019-06-17 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0032_auto_20190617_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 19, 16, 43, 700263)),
        ),
    ]