# Generated by Django 2.0.13 on 2019-06-17 15:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0031_auto_20190616_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='CategoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stronka.Category'),
        ),
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 17, 37, 54, 580085)),
        ),
    ]
