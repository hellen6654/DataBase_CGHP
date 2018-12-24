from django.contrib import admin
from .models import OrderItem, Order, Discount, DiscountFare, DiscountOrder
from .forms import DiscountFareForm, DiscountFareInlineFormSet

'''
https://stackoverflow.com/questions/1732151/override-save-model-on-django-inlinemodeladmin
https://stackoverflow.com/questions/28515470/wsgirequest-object-has-no-attribute-get
https://stackoverflow.com/questions/1470811/django-disallow-can-delete-on-genericstackedinline
'''

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['pizza']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'member_id', 'ordered_date', 'updated', 'paid', 'shipped_date']
    list_filter = ['paid', 'ordered_date', 'updated']
    inlines = [OrderItemInline]

class DiscountFareInline(admin.TabularInline):
    model = DiscountFare
    form = DiscountFareForm
    formset = DiscountFareInlineFormSet
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(DiscountFareInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

class DiscountOrderInline(admin.TabularInline):
    model = DiscountOrder

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name','kind','description',]
    inlines = [DiscountFareInline, DiscountOrderInline,]