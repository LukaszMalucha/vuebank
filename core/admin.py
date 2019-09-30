from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core.models import CustomUser


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'usernaname']
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_vip')
    search_fields = ['email', 'usernaname']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('usernaname',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_vip')}),
        (_('Important dates'), {'fields': ('last_login',)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)  # Coma - TUPLE!


admin.site.register(CustomUser, UserAdmin)