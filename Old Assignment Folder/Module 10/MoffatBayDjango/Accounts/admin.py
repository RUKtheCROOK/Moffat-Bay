from django.contrib import admin
from .models import CustomUser

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the admin page for the CustomUser model. It displays the user's ID, first name, last name, email, phone number, created date, last login date, and permissions.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['userID', 'first_name', 'last_name', 'email', 'phone', 'created_date', 'last_login', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['created_date', 'last_login', 'is_staff', 'is_superuser', 'is_active']
    fieldsets = [
        ('User Information', {'fields': ['first_name', 'last_name', 'email', 'phone']}),
        ('Password Information', {'fields': ['password_hash', 'password_salt']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('Date Information', {'fields': ['created_date', 'last_login']}),
    ]
    readonly_fields = ['created_date', 'last_login']
    ordering = ['created_date']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # You can customize the form here if needed
        return form