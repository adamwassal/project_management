# Generated by Django 5.0.6 on 2024-06-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_companydata_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydata',
            name='address',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='companydata',
            name='details',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
