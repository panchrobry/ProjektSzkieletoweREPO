# Generated by Django 2.0.13 on 2019-04-23 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0014_auto_20190409_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='ID',
        ),
        migrations.AddField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 23, 20, 52, 7, 369619)),
        ),
    ]
