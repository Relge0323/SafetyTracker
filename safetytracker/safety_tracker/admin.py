from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the User model

    - display key user info in the list view: 'username', 'email', 'role', 'is_staff', and 'is_active'

    - add sidebar filters for role, staff status and active status

    - provide search box for username and email fields
    """
    
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')