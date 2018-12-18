from django.urls import path
from . import views

urlpatterns = [
    path('', views.Create_Member_View, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register_Member/', views.Create_Member_View, name='Create_Member_View'),
    path('register_Employee/', views.Create_Employee_View, name='Create_Employee_View'),
]