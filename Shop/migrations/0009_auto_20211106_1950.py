# Generated by Django 3.0.8 on 2021-11-06 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20211106_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 6, 19, 50, 6, 422505)),
        ),
    ]
