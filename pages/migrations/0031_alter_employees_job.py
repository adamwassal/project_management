# Generated by Django 5.0.6 on 2024-06-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_employees_cv_employees_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='job',
            field=models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Data Analyst', 'Data Analyst'), ('Project Manager', 'Project Manager'), ('HR Specialist', 'HR Specialist'), ('Data Scientist', 'Data Scientist'), ('UX Designer', 'UX Designer'), ('mMrketing Director', 'Marketing Director'), ('Sales Director', 'Sales Director')], max_length=400, null=True),
        ),
    ]
