from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Employees, Tasks, CompanyData, VacationRequest, Profites
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
import datetime
from django.utils import timezone

# Create your views here.

@login_required(login_url='login/')
def dashboard(request):
    employees_count = Employees.objects.all().count()

    tasks_count = Tasks.objects.filter(user = request.user).count()
    tasks_count_completed = Tasks.objects.filter(user = request.user,complete = 'True').count()
    tasks_count_uncompleted = Tasks.objects.filter(user = request.user,complete = 'False').count()

    
    data_tasks = {
                'labels': ['Completed tasks', 'Uncompleted tasks'],
                'data': [int(tasks_count_completed), int(tasks_count_uncompleted)],
            }
    context = {
        'users':str(User.objects.all().count()),
        'usernames':User.objects.all(),
        'employees':str(employees_count), 
        'tasks':str(tasks_count),
        'com_tasks':str(Tasks.objects.filter(user=request.user, complete=True).count()),
        'data_tasks':data_tasks,
        'cd':CompanyData.objects.all(),
        'pagetitle':'Dashboard',
    }

    return render(request,'pages/dashboard.html', context)

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/'

    def get_success_url(self):
        return '/'
    
class SignUpView(CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
    
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login/')
def all_users(request):
    if request.user.is_superuser:
        data= {
            'labels': ['Admin users', 'Normal users'],
            'data': [User.objects.filter(is_superuser=True).count(), User.objects.filter(is_superuser=False).count()],
        }
        return render(request, 'pages/all_users.html', {'users':User.objects.all(), 'data':data, 'all_users':User.objects.all().count(),'cd':CompanyData.objects.all(),'pagetitle':'All users'})
    else:
        return render(request, 'pages/all_users.html')


class CompanyDataView(LoginRequiredMixin, CreateView, ListView):
    model = CompanyData
    template_name = 'accounts/companydata.html'
    success_url = '/mycompany/'
    login_url = 'login/'
    form_class = forms.CompanyForm
    context_object_name = 'data'

    def form_valid(self, form):
        # Optionally, you can customize behavior here before saving
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_count'] = Employees.objects.all().count()
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'My Company'
        return context
    
class CompanyDataUpdate(LoginRequiredMixin, UpdateView):
    model = CompanyData
    template_name = 'accounts/update_cdata.html'
    success_url = '/mycompany'
    login_url = '/login'
    form_class = forms.CompanyUpdateData
    context_object_name = 'update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Update Your company data'
        return context
    
@login_required(login_url='login/')
def profile(request):

    if request.method == 'POST':
        x = request.POST.get('email')
        y = request.POST.get('fname')
        z = request.POST.get('lname')
        c = request.POST.get('job')
        request.user.email = x
        request.user.first_name = y
        request.user.last_name = z
        request.user.job = c
        
        request.user.save()
        return redirect('profile')

    return render(request,'accounts/profile.html',{'cd':CompanyData.objects.all(),'pagetitle':'My profile'})

@login_required(login_url='login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('/profile')
       
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {
        'form': form,
        'cd':CompanyData.objects.all(),
        'pagetitle':'Change password'
    })


class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/users_profile.html'
    context_object_name = 'u'
    login_url = 'login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'User Details'
        return context
    
def company_profits(request):
    context = {
        'employees_salaries':Employees.objects.all(),
        'profits':False,
        'total':False,
        'cd':CompanyData.objects.all(),
        'pagetitle':'Company Profits',
    }
    
    if request.method == 'POST':
        if 'profits' in request.POST:
            x = request.POST.get('profits')
            y = request.POST.get('water')
            z = request.POST.get('gas')
            r = request.POST.get('transport')
            if x and y and z and r:
                Profites.objects.create(earn = x, water=y, gas = z, transport = r)
                t = sum(employee.salary for employee in context['employees_salaries'])
                context['total'] = t
                context['profits'] = int(x) - t
                context['x'] = x
                
                context['y'] = y
                context['z'] = z
                context['r'] = r
                context['to'] = int(y) + int(z) + int(r)
                context['t'] = int(context['profits']) - int(y) - int(z) - int(r)
                
                if context['profits'] and context['total']:
                    data = {
                        'labels': ['Earn%', 'Salaries%', 'Other costs'],
                        'data': [
                            context['profits'] / int(x) * 100,
                            context['total'] / int(x) * 100,
                            context['to'] / int(x) * 100,
                        ],
                    }
                    context['data'] = data

    return render(request, 'pages/company_profits.html', context)


class VacationRequestView(LoginRequiredMixin, CreateView):
    model = VacationRequest
    template_name = 'employees/vacationrequest.html'
    success_url = '/'
    login_url = '/login'
    form_class = forms.VacationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['data'] = VacationRequest.objects.filter(user=self.request.user)
        context['pagetitle'] = 'Create Vacation Request'
        context['now'] = timezone.now() - timezone.timedelta(days=2)
        return context
    
class VacationRequestViewDelete(LoginRequiredMixin, DeleteView):
    model = VacationRequest
    template_name = 'employees/delete_vacation.html'
    success_url = '/'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Delete Your request'
        return context
    

class AllVacationRequests(LoginRequiredMixin, ListView):
    model = VacationRequest
    template_name = 'employees/allvacation.html'
    login_url = '/login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests_all'] = VacationRequest.objects.all()
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Vacation Requests'
        context['now'] = timezone.now() - timezone.timedelta(days=2)
        context['users_'] = User.objects.all()
        context['users'] = []
        for i in context['users_']:
            context['users'].append(i.username)
        return context
    
@require_POST
def update_accept(request, pk):
    vacation_request = get_object_or_404(VacationRequest, pk=pk)
    vacation_request.accept = True  # Example update
    vacation_request.save()
    return redirect('/allvacationrequests')  # Redirect to a desired page after updating

def delete_vacation(request, pk):
    vacation_request = get_object_or_404(VacationRequest, pk=pk)
    vacation_request.delete()
    return redirect('/')  # Redirect to a desired page after updating

