from django.contrib import admin
from .models import Pizza
# Register your models here.
@admin.register(Pizza)
class UserAdmin(admin.ModelAdmin):
    pass
