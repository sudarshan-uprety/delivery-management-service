from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'full_name')