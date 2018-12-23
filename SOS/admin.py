from django.contrib import admin
from .models import OrderItem, Order
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['pizza']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['order_no', 'member_id', 'ordered_date', 'updated', 'paid', 'shipped_date']
    list_filter = ['paid', 'ordered_date', 'updated']
    inlines = [OrderItemInline]
    '''
    def getMemberEmail(self, obj):
        return obj.member_id.user_id.email

    getMemberEmail.admin_order_field = 'user_id'
    getMemberEmail.short_description = 'email'
    '''
