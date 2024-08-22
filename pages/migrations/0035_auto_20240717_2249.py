# Generated by Django 3.2.12 on 2024-07-17 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_vacationrequest_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 8, 16), null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.CharField(choices=[('admin', 'admin'), ('test', 'test'), ('tra', 'tra')], max_length=40, null=True),
        ),
    ]
