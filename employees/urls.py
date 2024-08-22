from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeView.as_view(), name='employees'),
    path('<pk>/details', views.DetailView.as_view(), name='detail_employee'),
    path('create/', views.EmployeeCreate.as_view(), name='create_employee'),
    path('<pk>/delete', views.EmployeeDelete.as_view(), name='delete_employee'),
    path('<pk>/update', views.EmployeeUpdate.as_view(), name='update_employee'),

    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('alltasks/', views.AllTasksView.as_view(), name='alltasks'),
    path('tasks/<pk>/details', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='create_task'),
    path('tasks/<pk>/delete', views.TaskDelete.as_view(), name='delete_task'),
    path('tasks/<pk>/update', views.TaskUpdate.as_view(), name='update_task'),
    path('task/<pk>/delete', views.delete_task, name='deletetaskfast'),
]