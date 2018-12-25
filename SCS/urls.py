from django.urls import path
from .views import cart_add, cart_remove,cart_detail
urlpatterns = [
    path('', cart_detail, name='cart'),
    path('add/<int:pizza_id>', cart_add, name='cart_add'),
    path('remove/<int:pizza_id>', cart_remove, name='cart_remove'),
]