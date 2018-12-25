from django.contrib import admin
from .models import OrderItem, Order, Discount, DiscountFare, DiscountOrder
from .forms import DiscountFareForm, DiscountOrderForm, DiscountInlineFormSet

'''
https://stackoverflow.com/questions/1732151/override-save-model-on-django-inlinemodeladmin
https://stackoverflow.com/questions/28515470/wsgirequest-object-has-no-attribute-get
https://stackoverflow.com/questions/1470811/django-disallow-can-delete-on-genericstackedinline
https://stackoverflow.com/questions/6506439/django-change-inlines-based-on-select-option
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
    formset = DiscountInlineFormSet
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(DiscountFareInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

class DiscountOrderInline(admin.TabularInline):
    model = DiscountOrder
    form = DiscountOrderForm
    formset = DiscountInlineFormSet
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(DiscountOrderInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name','kind','description',]
    inlines = [DiscountFareInline, DiscountOrderInline,]
