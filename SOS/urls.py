from django.urls import path

from .views import order_create, order_history,order_detail

urlpatterns = [ 
    path('create/', order_create, name='order_create'), 
    path('orderHistory/', order_history, name='order_history'),
    path('orderDetail/<int:order_no>/', order_detail, name='order_detail')
]