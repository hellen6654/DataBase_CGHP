from django.shortcuts import render
from MCS.models import IsInGroup
from SCS.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem
# Create your views here.

def order_create(request):
    cart = Cart(request)
    isError = False
    if request.method == 'POST':
        isMember = IsInGroup(user=request.user, groupName='Member')
        isError = not isMember
        form = OrderCreateForm(request.POST)
        if form.is_valid() and isMember:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, pizza=item['pizza'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()# clear the cart
            return render(request, 'created.html',{'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html',{'cart': cart, 'form': form, 'isError': isError})

