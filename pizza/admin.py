from django.contrib import admin
from .models import Pizza,User
# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass