from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_vip')
    search_fields = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_vip')}),
        (_('Important dates'), {'fields': ('last_login',)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)  # Coma - TUPLE!


class InstrumentModelAdmin(admin.ModelAdmin):
    list_display = ["name", "symbol", "category", "price"]
    list_filter = ("category",)
    search_fields = ["symbol", "name"]

    class Meta:
        model = models.Instrument


class AssetModelAdmin(admin.ModelAdmin):
    ordering = ['owner', 'instrument']
    list_display = ["owner", "instrument", "quantity", "value"]
    list_filter = ('instrument',)
    search_fields = ["owner", "instrument"]

    class Meta:
        model = models.Asset

class BuyTransactionModelAdmin(admin.ModelAdmin):
    ordering = ['owner', 'created_at']
    list_display = ["owner", "instrument", "quantity", "value", "created_at"]
    list_filter = ('instrument', ('created_at', DateRangeFilter))  # datetime search add-on
    search_fields = ["owner", "instrument"]

    class Meta:
        model = models.BuyTransaction


class SellTransactionModelAdmin(admin.ModelAdmin):
    ordering = ['owner', 'created_at']
    list_display = ["owner", "instrument", "quantity", "value", "created_at"]
    list_filter = ('instrument', ('created_at', DateRangeFilter))
    search_fields = ["owner", "instrument"]

    class Meta:
        model = models.SellTransaction

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Instrument, InstrumentModelAdmin)
admin.site.register(models.Asset, AssetModelAdmin)
admin.site.register(models.BuyTransaction, BuyTransactionModelAdmin)
admin.site.register(models.SellTransaction, SellTransactionModelAdmin)
