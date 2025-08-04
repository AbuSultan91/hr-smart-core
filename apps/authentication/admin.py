"""
HR Smart Core - Authentication Admin
إعدادات إدارة المصادقة
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Role, UserRole, LoginLog


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'ملف المستخدم'
    fields = ['phone', 'avatar', 'language', 'timezone']


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']


# إعادة تسجيل UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    filter_horizontal = ['permissions']


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'company', 'granted_by', 'is_active', 'granted_at']
    list_filter = ['role', 'company', 'is_active', 'granted_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    autocomplete_fields = ['user', 'role', 'company', 'granted_by']


@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip_address', 'login_time', 'logout_time', 'is_successful']
    list_filter = ['is_successful', 'login_time']
    search_fields = ['user__username', 'ip_address']
    readonly_fields = ['user', 'ip_address', 'user_agent', 'login_time', 'logout_time', 'is_successful', 'failure_reason']
    
    def has_add_permission(self, request):
        return False  # منع إضافة سجلات يدوياً
    
    def has_change_permission(self, request, obj=None):
        return False  # منع تعديل السجلات
