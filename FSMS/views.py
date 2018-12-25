from django.shortcuts import render
from SOS.models import Order, OrderItem
from .models import CheckOrder
from MCS.models import Employee
import datetime
# Create your views here.


def check_order(request):
    total_order = Order.objects.all()
    total_orderitem = OrderItem.objects.all()
    return render(request, 'checkorder_detail.html', locals())


def money_report(request):
    total_order = Order.objects.all()
    total_result = CheckOrder.objects.all()
    total_profits = 0
    today = datetime.datetime.now()

    year_result = []
    for year in range(2015, today.year+1):
        temp = []
        temp.append(year)
        buf = 0
        for checkorder in total_result:
            if str(year) == str(Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.year):
                buf += checkorder.profits
        temp.append(buf)
        year_result.append(temp)

    month_result = []
    for year in range(2015, today.year+1):
        for month in range(1, 13):
            temp = []
            temp.append(year)
            temp.append(month)
            buf = 0
            for checkorder in total_result:
                if str(year) == str(Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.year):
                    if str(month) == str(Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.month):
                        buf += checkorder.profits
            temp.append(buf)
            month_result.append(temp)

    day_result = []
    for date in range(1, 32):
        temp = []
        temp.append(today.year)
        temp.append(today.month)
        temp.append(date)
        buf = 0
        for checkorder in total_result:
            if today.year == Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.year:
                if today.month == Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.month:
                    if date == Order.objects.get(order_no=checkorder.order_no.order_no).ordered_date.day:
                        buf += checkorder.profits
        temp.append(buf)
        day_result.append(temp)

    for order in total_result:
        total_profits += order.profits

    employee_result = []
    for employee in Employee.objects.all():
        temp=[]
        temp.append(Employee.objects.get(user_id=employee.user_id))
        buf = 0

        for checkorder in total_result:
            if checkorder.employee_id == Employee.objects.get(user_id=employee.user_id):
                buf += checkorder.profits
        temp.append(buf)
        employee_result.append(temp)
        
    return render(request, 'money_report.html', locals())
