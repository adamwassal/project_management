from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from pages.models import Employees, Tasks, CompanyData
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pages.forms import EmloyeeForm, TasksForm, EmployeeBulkDeleteForm, TasksBulkDeleteForm, UpdateTasksForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

class EmployeeView(LoginRequiredMixin, ListView):
    model = Employees
    template_name = 'employees/employees.html'
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = EmployeeBulkDeleteForm(request.POST)
        if form.is_valid():
            employees = form.cleaned_data['employees']
            select = form.data['selection']
            if select == 'delete':
                employees.delete()
            return redirect('/employees')
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_count'] = Employees.objects.all().count()
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Employees'
        return context


class DetailView(LoginRequiredMixin,DetailView):
    model = Employees
    template_name = 'employees/employee_detail.html'
    context_object_name = 'detail'
    login_url = '/login'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Employee Details'
        return context

    
class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employees
    template_name = 'employees/delete_employee.html'
    success_url = '/employees'
    context_object_name = 'delete'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Delete Employee'
        return context


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employees
    template_name = 'employees/update_employee.html'
    success_url = '/employees'
    login_url = '/login'
    form_class = EmloyeeForm
    context_object_name = 'update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Update Employee'
        return context


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employees
    template_name = 'employees/create_employee.html'
    success_url = '/employees'
    login_url = '/login'
    form_class = EmloyeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Create Employee'
        return context



class TaskDetailView(DetailView,LoginRequiredMixin):
    model = Tasks
    template_name = 'tasks/employee_task.html'
    context_object_name = 'detail'
    login_url = '/login'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Task Details'
        return context


class TasksView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/tasks.html'
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = TasksBulkDeleteForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data['tasks']
            select = form.data['selection']
            if select == 'complete':
                tasks.update(complete = True)
            elif select == 'delete':
                tasks.delete()
            return redirect('tasks')
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_count'] = Tasks.objects.filter(user=self.request.user).count()
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Tasks'
        context['now'] = timezone.now()
        return context
    
class AllTasksView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/alltasks.html'
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = TasksBulkDeleteForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data['tasks']
            select = form.data['selection']
            if select == 'complete':
                tasks.update(complete = True)
            elif select == 'delete':
                tasks.delete()
            return redirect('tasks')
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_count'] = Tasks.objects.all().count()
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'All Tasks'
        context['now'] = timezone.now()
        context['users_'] = User.objects.all()
        context['users'] = []
        for i in context['users_']:
            context['users'].append(i.username)        
        return context
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete_task.html'
    success_url = '/employees/tasks'
    context_object_name = 'delete'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Delete task'
        return context

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update_task.html'
    success_url = '/employees/tasks'
    login_url = '/login'
    form_class = UpdateTasksForm
    context_object_name = 'update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Update task'
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'tasks/create_task.html'
    success_url = '/employees/tasks'
    login_url = '/login'
    form_class = TasksForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cd'] = CompanyData.objects.all()
        context['pagetitle'] = 'Create Task'
        return context

def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect('/alltasks')  # Redirect to a desired page after updating