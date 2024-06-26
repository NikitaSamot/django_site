from re import search
from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

from .models import User
# Register your models here.



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username']
    search_fields = ['first_name', 'last_name', 'email', 'username']
    inlines = [CartTabAdmin, OrderTabulareAdmin]
    