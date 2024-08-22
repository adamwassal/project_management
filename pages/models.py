from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, timedelta
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()
users = []

allusers = User.objects.all()

for i in allusers:
    users.append((i.username, i.username))

class Employees(models.Model):
    name = models.CharField(max_length = 51)
    birth = models.DateField(null = True)
    address = models.TextField(max_length = 400, null=True)
    mobile1 = PhoneNumberField(null=True,unique=True)
    mobile2 = PhoneNumberField(null=True,blank=True,unique=True)
    email = models.CharField(max_length = 400, null=True)
    job = models.CharField(max_length = 400, null=True, choices = [
        ('Software Engineer','Software Engineer'),
        ('Data Analyst','Data Analyst'),
        ('Project Manager','Project Manager'),
        ('HR Specialist','HR Specialist'),
        ('Data Scientist','Data Scientist'),
        ('UX Designer','UX Designer'),
        ('mMrketing Director','Marketing Director'),
        ('Sales Director','Sales Director'),
    ])
    start_date = models.DateField(null=True, default = date.today() + timedelta(days=30))
    employment_type = models.CharField(max_length = 400, null=True, choices= [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
    ])
    work_schedule = models.IntegerField(null=True,validators=[MaxValueValidator(24),MinValueValidator(1)],verbose_name = 'Work Schedule(hours)')
    salary = models.IntegerField(null=True)
    cv = models.ImageField(upload_to='photos/cvs', null=True, blank=True)
    

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    user = models.CharField(max_length = 40,choices=users, blank=True, null=True, default=User.username)
    name = models.CharField(max_length = 50)
    complete = models.BooleanField(null=True, default=False)
    date = models.DateTimeField(default = datetime.datetime.now)
    willdate = models.DateTimeField(verbose_name = 'will complete it in')


class CompanyData(models.Model):
    logo = models.ImageField(upload_to='photos/', null=True)
    company_name = models.CharField(max_length=100, null=True)
    details = models.TextField(max_length=600, null=True, blank=True)
    address = models.CharField(max_length=600, null=True, blank=True)
    manager_name = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.company_name
    

class VacationRequest(models.Model):
    user = models.CharField(max_length = 40, null=True)
    date = models.DateTimeField(default = datetime.datetime.now)
    email = models.CharField(max_length = 100, null=True)
    accept = models.BooleanField(null=True)
    

class Profites(models.Model):
    earn = models.IntegerField(null=True)
    water = models.IntegerField(null=True)
    gas = models.IntegerField(null=True)
    transport = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.earn)