from django.contrib import admin

from password_manager.models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user')
    readonly_fields = ('created_at', 'updated_at')
