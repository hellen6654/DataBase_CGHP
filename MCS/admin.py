# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):
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
            'fields': ('email', 'password1', 'password2','last_name', 'first_name','id_TW','phone_number','address','age','gender','discount','groups'),
        }),
    )
    list_display = ('email', 'last_name', 'first_name')
    search_fields = ('email', 'last_name''first_name')
    ordering = ('email','id_TW',)