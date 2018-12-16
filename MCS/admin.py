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
    list_display = ('email', 'last_name','first_name')
    #search_fields = ('email', 'last_name','first_name')
    ordering = ('email','id_TW')

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


#admin.site.register(CustomUser, CustomUserAdmin)
'''
class EmployeeInline(admin.StackedInline):
    model = Employee

class MemberInline(admin.StackedInline):
    model = Member

#@admin.register(Member)
class CustomUserAdmin(CustomUserAdmin):
    inlines = [MemberInline, EmployeeInline]

admin.site.register(CustomUser, CustomUserAdmin)
'''