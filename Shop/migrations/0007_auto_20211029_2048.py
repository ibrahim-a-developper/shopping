# Generated by Django 3.0.8 on 2021-10-29 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_auto_20211028_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 29, 20, 48, 42, 904937)),
        ),
    ]
