from django.contrib import admin

from .models import MilkOrder, OrderAssignment

from django.contrib import admin
from .models import MilkOrder, OrderAssignment

@admin.register(MilkOrder)
class MilkOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'milk_type', 'quantity', 'order_at')
    list_filter = ('milk_type', 'order_at')
    search_fields = ('user__email',)

@admin.register(OrderAssignment)
class OrderAssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'staff_member', 'status')
    list_filter = ('status', 'staff_member')
    search_fields = ('order__user__email',)
