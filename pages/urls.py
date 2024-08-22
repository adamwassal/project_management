from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('allusers/', views.all_users, name='all_users'),
    path('mycompany/', views.CompanyDataView.as_view(), name='company'),
    path('mycompany/<pk>/update/', views.CompanyDataUpdate.as_view(), name='companyupdate'),
    path('profile/', views.profile, name='profile'),
    path('<pk>/profile/', views.UserDetailView.as_view(), name='user_profile'),
    path('changepassword/', views.change_password, name='change_password'),
    path('companyprofits/', views.company_profits, name='companyprofits'),
    path('vacationrequest/', views.VacationRequestView.as_view(), name='vacation'),
    path('vacationrequest/<pk>/delete', views.VacationRequestViewDelete.as_view(), name='vacationdelete'),
    path('allvacationrequests/', views.AllVacationRequests.as_view(), name='avr'),
    path('allvacationrequests/<pk>/update', views.update_accept, name='updatevacation'),
    path('vaction/<pk>/delete', views.delete_vacation, name='deletevacation'),
]