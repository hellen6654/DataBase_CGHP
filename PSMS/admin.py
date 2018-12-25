from django.contrib import admin
from .models import Pizza
# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['pizza_no', 'name', 'element', 'description', 'price',
        'size', 'cost', 'in_stock', 'sales_volume', 'click_count', 'kind',
        'stars', 'pic', 'available', 'slug']
    list_filter = ['available', 'kind']
    list_editable = ['price', 'size', 'cost', 'in_stock', 'available']
    prepopulated_fields = {'slug':('pizza_no',)}
