from django.contrib import admin
from .models import CheckOrder
# Register your models here.

@admin.register(CheckOrder)
class CheckOrderAdmin(admin.ModelAdmin):
    pass