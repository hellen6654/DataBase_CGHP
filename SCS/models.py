from decimal import Decimal
from django.db import models
from django.conf import settings
from PSMS.models import Pizza

# Create your models here.

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, pizza, quantity=1, update_quantity=False):
        pizza_id = str(pizza.pizza_no)
        if pizza_id not in self.cart:
            self.cart[pizza_id] = {'quantity':0, 'price': str(pizza.price)}
        if update_quantity:
            self.cart[pizza_id]['quantity'] = quantity
        else:
            self.cart[pizza_id]['quantity'] += quantity
        self.save()

    def remove(self, pizza):
        pizza_id = str(pizza.pizza_no)
        if pizza_id in self.cart:
            del self.cart[pizza_id]
            self.save()

    def __iter__(self):
        pizza_ids = self.cart.keys()
        pizzas = Pizza.objects.filter(pizza_no__in=pizza_ids)
        for pizza in pizzas:
            self.cart[str(pizza.pizza_no)]['pizza'] = pizza
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
               self.cart.values())
               
    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True