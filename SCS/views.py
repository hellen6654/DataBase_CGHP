from django.shortcuts import redirect,get_object_or_404,render
from django.views.decorators.http import require_POST
from PSMS.models import Pizza
from SCS.models import Cart
from SCS.forms import CartAddProductForm
# Create your views here.

@require_POST
def cart_add(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(pizza=pizza, quantity=cd['quantity'],
        update_quantity=cd['update'])
    return redirect('cart')

def cart_remove(request, pizza_id):
    cart = Cart(request)
    pizza= get_object_or_404(Pizza, pk=pizza_id)
    cart.remove(pizza)
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity':item['quantity'], 'update':True})
    return render(request, 'cart.html', {'cart': cart})




