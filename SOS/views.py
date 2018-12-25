from django.shortcuts import render, redirect
from django.utils import timezone
from MCS.models import IsInGroup
from SCS.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from MCS.models import Member, Employee
from PSMS.models import *
from FSMS.models import CheckOrder
import math
from decimal import Decimal
# Create your views here.


def order_create(request):
    cart = Cart(request)
    isError = False
    discount = 0
    if cart.get_total_price(discount) >= 1000:
        discount = 60
    else:
        discount = 0
    total_price = cart.get_total_price(60-discount)
    if request.method == 'POST':
        isMember = IsInGroup(user=request.user, groupName='Member')
        isError = not isMember

        if isMember:
            member = Member.objects.get(user_id=request.user)
            order = Order.objects.create(member_id=member)
            order.save()
            for item in cart:
                pizza = item['pizza']
                pizza.in_stock-=item['quantity']
                if pizza.in_stock == 0:
                    pizza.available=False
                pizza.save()
                OrderItem.objects.create(order=order, pizza=item['pizza'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()  # clear the cart
            return render(request, 'created.html', {'order': order})
    return render(request, 'create.html', locals())


def order_history(request):
    member = Member.objects.get(user_id=request.user)
    result = []
    for order in Order.objects.all():
        if order.member_id == member:
            result.append(order)
    return render(request, 'order_history.html', locals())


def order_detail(request, order_no):
    order = Order.objects.get(order_no=order_no)
    orderitem = OrderItem.objects.filter(order=order)

    if request.method == 'POST':
        order.paid = True
        order.shipped_date = timezone.now()
        CheckOrder.objects.create(order_no=order, empolyee_id=Employee.objects.get(user_id=request.user),
                                  profits=order.get_total_cost())
        return redirect('check_order')

    return render(request, 'order_detail.html', locals())
