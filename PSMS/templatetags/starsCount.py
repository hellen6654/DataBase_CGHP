from django.template import Library

register = Library()

@register.filter
def starsCount(pizza):
    return pizza.starsCounter()