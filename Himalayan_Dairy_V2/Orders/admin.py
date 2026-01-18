from django.contrib import admin
from .models import MilkOrder

@admin.register(MilkOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'milk_type', 'quantity', 'status', 'order_at')
    list_filter = ('milk_type', 'status', 'order_at')
    search_fields = ('user__email', 'milk_type')