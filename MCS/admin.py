from django.contrib import admin
from .models import User, Member
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    pass
