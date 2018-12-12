from django.views.generic import ListView, DetailView
from .models import Pizza
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'index.html')
def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request,'menu-list.html',{'pizzas':pizzas})