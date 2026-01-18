from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ("email","first_name","last_name","phone","is_staff","is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    
    search_fields = ("email","phone","first_name","last_name")
    ordering=("email",)
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info",{
            "fields":(('first_name','middle_name','last_name'),),
            "description":"Basic details of the dairy member."
        }),
        ("Contact Details",{
            "fields":('phone',),
        }),
        ("Roles & Status", {
            "fields": ( "is_staff", "is_active", "is_superuser"),
        }),
        
        ("Advanced Permissions", {
            "classes": ("collapse",),
            "fields": ("groups", "user_permissions"),
        }),
        
        ("Important Dates", {
            "fields": ("last_login", "date_joined"),
        }),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone", "password", "confirm_password"), 
        }),
    )
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets
    
