# Generated by Django 2.0.13 on 2019-06-07 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronka', '0020_auto_20190608_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Register_Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 8, 0, 37, 48, 37055)),
        ),
    ]
