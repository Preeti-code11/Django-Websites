from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'ordered_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'product__title')

