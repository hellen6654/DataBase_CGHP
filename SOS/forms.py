from django import forms
from django.forms.models import BaseInlineFormSet
from .models import Order, Discount, DiscountFare, DiscountOrder

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['member_id']

class DiscountFareForm(forms.ModelForm):
    class Meta:
        model = DiscountFare
        fields = ['sill']

class DiscountFareInlineFormSet(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        obj = super(DiscountFareInlineFormSet, self).save_new(form, commit=False)
        name = self.request.POST.get('name')
        obj.discount_code = Discount.objects.get(name=name)
        if commit:
            obj.save()
        return obj