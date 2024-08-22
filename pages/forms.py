from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employees, Tasks, CompanyData, VacationRequest, Profites


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

        widgets = {
            'password1':forms.widgets.PasswordInput(attrs={'id': 'password1'}),
            'password2':forms.widgets.PasswordInput(attrs={'id': 'password2'}),
        }


class EmloyeeForm(forms.ModelForm):
    class Meta():
        model = Employees
        fields = '__all__'
        widgets = {
            'birth':forms.widgets.DateInput(attrs={'type': 'date'}),
            'start_date':forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class CompanyUpdateData(forms.ModelForm):
    class Meta():
        model = CompanyData
        fields = '__all__'

class TasksForm(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = '__all__'
        widgets = {
            'date':forms.widgets.DateTimeInput(attrs={'readonly':True}),
            'willdate':forms.widgets.DateTimeInput(attrs={'type':'date'}),
            'complete':forms.CharField.widget(attrs={'disabled':True}),
            'user': forms.widgets.Select(attrs={'id':'userr'})
        }

class UpdateTasksForm(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = '__all__'
        widgets = {
            'date':forms.widgets.DateTimeInput(attrs={'readonly':True}),
            'willdate':forms.widgets.DateTimeInput(attrs={'readonly':True}),
            'user': forms.widgets.Select(attrs={'id':'userr'}),
            'name':forms.CharField.widget(attrs={'readonly':True})
        }
        

class EmployeeBulkDeleteForm(forms.Form):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employees.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class TasksBulkDeleteForm(forms.Form):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Tasks.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class CompanyForm(forms.ModelForm):
    class Meta():
        model = CompanyData
        fields = '__all__'
        widgets = {
            'logo': forms.FileField.widget(attrs={'accept':'photos/*'})
        }

class VacationForm(forms.ModelForm):
    class Meta():
        model = VacationRequest
        fields = '__all__'

        widgets = {
            'accept': forms.widgets.HiddenInput(),
            'user': forms.CharField.widget(attrs={'id':'user', 'readonly':'true'}),
            'email': forms.EmailField.widget(attrs={'id':'email', 'readonly':'true'}),
            'date': forms.DateTimeField.widget(attrs={'readonly':'true'}),
        }
        
class ProfitsForm(forms.ModelForm):
    class Meta():
        model = Profites
        fields = '__all__'
