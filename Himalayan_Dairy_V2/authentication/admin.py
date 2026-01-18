from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     # Define which fields to display in the list view
#     list_display = ('email', 'phone', 'is_staff', 'is_active')
#     # Order by email instead of username
#     ordering = ('email',)
    
#     # This dictates the layout of the "Edit User" page
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('phone', 'first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
    
#     # Fields to show when creating a user
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'phone', 'password'),
#         }),
#     )

admin.site.register(CustomUser)