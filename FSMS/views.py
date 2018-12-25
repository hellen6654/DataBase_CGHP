from django.shortcuts import render
from SOS.models import Order,OrderItem
# Create your views here.

def check_order(request):
    total_order = Order.objects.all()
    total_orderitem = OrderItem.objects.all()
    return render(request,'checkorder_detail.html',locals())