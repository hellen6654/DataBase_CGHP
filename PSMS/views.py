from django.shortcuts import render
from .models import Pizza
# Create your views here.

def home(request):
    return render(request,'index.html')
def menu(request):
    pizzas = Pizza.objects.all()
    return render(request,'menu-list.html',{'pizzas':pizzas})
def about(request):
    return render(request,'about-us.html')