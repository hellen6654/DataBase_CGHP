from django.urls import path
from .views import  menu,detail

urlpatterns = [
    path('', menu, name='menu'),
    path('<int:no>/', detail, name='detail'),
]