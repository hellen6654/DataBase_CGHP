from django.shortcuts import render, get_object_or_404,redirect
from .models import Pizza
from SCS.forms import CartAddProductForm
from SCS.models import Cart
# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu-list.html', {'pizzas':pizzas})

def about(request):
    return render(request, 'about-us.html')

def detail(request, no):
    pizza = get_object_or_404(Pizza, pk=no)
    cates = pizza.kind_chose
    return render(request, 'menu-details.html', {'pizza':pizza, 'cates':cates})

def search(request):
    pizzas = Pizza.objects.all()
    if request.method == 'POST':
        search=request.POST['element']
        pizza_no=[]
        for pizza in Pizza.objects.all():
            pizza_element = pizza.element.split(',')
            for element in pizza_element:
                if search in element:
                    pizza_no.append(pizza.pizza_no)
        return render(request ,'search.html',locals())