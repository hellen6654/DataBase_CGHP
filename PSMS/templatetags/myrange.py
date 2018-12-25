from django import template

register = template.Library()


@register.filter
def myrange(value):
    return range(1, value+1)