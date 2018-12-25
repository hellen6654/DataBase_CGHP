from django.urls import path

from .views import check_order, money_report

urlpatterns = [ 
    path('', check_order, name='check_order'), 
    path('moneyreport/', money_report, name='money_report')
]