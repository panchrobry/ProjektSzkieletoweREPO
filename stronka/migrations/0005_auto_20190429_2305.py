# Generated by Django 2.0.13 on 2019-04-29 21:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0004_auto_20190429_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stronka.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userown',
            name='TeamID',
        ),
        migrations.RemoveField(
            model_name='userown',
            name='user',
        ),
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 23, 5, 9, 505955)),
        ),
        migrations.DeleteModel(
            name='UserOwn',
        ),
    ]