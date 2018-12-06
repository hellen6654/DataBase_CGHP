from django.contrib import admin
from .models import Rate
from MCS.models import Employee
# Register your models here.
@admin.register(Rate)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    pass
