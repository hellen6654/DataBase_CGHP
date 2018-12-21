from django.shortcuts import render, get_object_or_404
from .models import Pizza
from MCS.views import MCS_View
# Create your views here.

def home(request):
    return render(request, 'index.html')
    #return MCS_View(request, 'index.html')

def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu-list.html', {'pizzas':pizzas})

def about(request):
    return render(request, 'about-us.html')

def detail(request, no):
    pizza = get_object_or_404(Pizza, pk=no)
    cates = pizza.kind_chose
    return render(request, 'menu-details.html', {'pizza':pizza, 'cates':cates})