from django.contrib import admin

from password_manager.models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
