from django.urls import path

from .views import check_order

urlpatterns = [ 
    path('', check_order, name='check_order'), 
    
]