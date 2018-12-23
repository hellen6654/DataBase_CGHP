from django.shortcuts import render
from MCS.models import IsInGroup
from SCS.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem,Order
from MCS.models import Member
# Create your views here.

def order_create(request):
    cart = Cart(request)
    isError = False
    mem=Member.objects.get(user_id = request.user)
    if request.method == 'POST':
        isMember = IsInGroup(user=request.user, groupName='Member')
        isError = not isMember
        if isMember:
            order = Order.objects.create(member_id=mem)
            for item in cart:
                OrderItem.objects.create(order=order, pizza=item['pizza'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()# clear the cart
            return render(request, 'created.html',{'order': order})
    return render(request, 'create.html',{'cart': cart, 'isError': isError})

