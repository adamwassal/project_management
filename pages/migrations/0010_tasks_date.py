# Generated by Django 5.0.6 on 2024-06-23 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_employees_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
