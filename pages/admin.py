from django.contrib import admin
from . import models

admin.site.register(models.Employees)
admin.site.register(models.Tasks)
admin.site.register(models.CompanyData)
admin.site.register(models.Profites)
# Register your models here.
