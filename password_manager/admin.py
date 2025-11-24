from django.contrib import admin

from password_manager.models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    pass
