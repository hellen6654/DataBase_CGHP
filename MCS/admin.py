# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser, Member, Employee

class CustomUserAdmin(DjangoUserAdmin):
    # 編輯使用者時顯示的欄位
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name','id_TW','phone_number','address','age','gender','discount')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # 新增 使用者會顯示的欄位
            'fields': ('email', 'password1', 'password2','last_name', 'first_name','id_TW','phone_number','address','age','gender','discount'),
        }),
    )
    list_display = ('email', 'id_TW', 'last_name','first_name',)
    ordering = ('email','id_TW',)

admin.site.register(CustomUser, CustomUserAdmin)

'''
https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
'''
class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display =('getUserEmail',)
    ordering = ('user_id',)
    search_fields = ('user_id',)

    def getUserEmail(self, obj):
        return obj.user_id.email

    getUserEmail.admin_order_field = 'user_id'
    getUserEmail.short_description = 'email'

admin.site.register(Member, MemberAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display =('getUserEmail', 'title', )
    ordering = ('user_id',)
    search_fields = ('user_id','title', )

    def getUserEmail(self, obj):
        return obj.user_id.email
    getUserEmail.admin_order_field = 'user_id'
    getUserEmail.short_description = 'email'
admin.site.register(Employee, EmployeeAdmin)