from django.shortcuts import render
from SCS.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, pizza=item['pizza'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()# clear the cart
            return render(request, 'created.html',{'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html',{'cart': cart, 'form': form})

