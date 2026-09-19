from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
@admin.register(User)
class UserAdminCustom(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("CRM", {"fields": ("role", "phone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("CRM", {"fields": ("role", "phone")}),)
