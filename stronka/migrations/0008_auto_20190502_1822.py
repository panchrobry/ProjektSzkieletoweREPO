# Generated by Django 2.0.13 on 2019-05-02 16:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stronka', '0007_auto_20190501_2104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserOwn',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 5, 2, 18, 22, 12, 787394)),
        ),
    ]
