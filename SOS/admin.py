from django.contrib import admin
from .models import OrderItem, Order
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['pizza']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'member_id', 'ordered_date', 'shipped_date','paid']
    list_filter = ['paid', 'ordered_date', 'member_id']
    inlines = [OrderItemInline]