"""
HR Smart Core - Companies Admin
إعدادات إدارة الشركات
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Company, Department, Position


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'commercial_registration', 'tax_number', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'commercial_registration', 'tax_number', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name', 'logo', 'commercial_registration', 'tax_number')
        }),
        ('معلومات الاتصال', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('الإعدادات', {
            'fields': ('settings', 'is_active')
        }),
        ('معلومات النظام', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'manager', 'parent_department', 'is_active', 'created_at']
    list_filter = ['company', 'is_active', 'created_at']
    search_fields = ['name', 'company__name']
    autocomplete_fields = ['company', 'manager', 'parent_department']
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('company', 'name', 'description')
        }),
        ('الهيكل التنظيمي', {
            'fields': ('parent_department', 'manager')
        }),
        ('الحالة', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'level', 'min_salary', 'max_salary', 'is_active']
    list_filter = ['department__company', 'level', 'is_active']
    search_fields = ['title', 'department__name', 'department__company__name']
    autocomplete_fields = ['department']
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('department', 'title', 'level')
        }),
        ('الوصف والمتطلبات', {
            'fields': ('description', 'requirements')
        }),
        ('معلومات الراتب', {
            'fields': ('min_salary', 'max_salary')
        }),
        ('الحالة', {
            'fields': ('is_active',)
        }),
    )
