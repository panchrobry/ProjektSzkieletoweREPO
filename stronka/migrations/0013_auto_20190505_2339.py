# Generated by Django 2.0.13 on 2019-05-05 21:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0012_auto_20190505_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 5, 5, 23, 39, 14, 961214)),
        ),
        migrations.AlterField(
            model_name='userown',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
