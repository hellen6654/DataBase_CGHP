from django.shortcuts import render
from .models import Pizza
from MCS.views import MCS_View
# Create your views here.

def home(request):
    return MCS_View(request, 'index.html')
def menu(request):
    pizzas = Pizza.objects.all()
    return render(request,'menu-list.html',{'pizzas':pizzas})
def about(request):
    return render(request,'about-us.html')