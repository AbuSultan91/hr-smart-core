"""
HR Smart Core - Employees Admin
إعدادات إدارة الموظفين
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Employee, EmployeeDocument


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'employee_id', 'get_full_name', 'company', 'department', 
        'position', 'status', 'hire_date'
    ]
    list_filter = [
        'company', 'department', 'status', 'gender', 
        'contract_type', 'hire_date', 'is_active'
    ]
    search_fields = [
        'employee_id', 'first_name', 'last_name', 'national_id', 
        'email', 'phone'
    ]
    autocomplete_fields = ['company', 'department', 'position', 'manager']
    readonly_fields = ['employee_id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('معرف الموظف', {
            'fields': ('employee_id',)
        }),
        ('معلومات الشركة', {
            'fields': ('company', 'department', 'position', 'manager')
        }),
        ('البيانات الشخصية', {
            'fields': (
                'national_id', 'first_name', 'last_name', 'email', 'phone',
                'birth_date', 'gender', 'nationality', 'address', 'profile_picture'
            )
        }),
        ('البيانات الوظيفية', {
            'fields': (
                'hire_date', 'contract_type', 'basic_salary', 
                'work_hours_per_day', 'work_days_per_week'
            )
        }),
        ('جهات الاتصال للطوارئ', {
            'fields': (
                'emergency_contact_name', 'emergency_contact_phone', 
                'emergency_contact_relation'
            ),
            'classes': ('collapse',)
        }),
        ('حالة الموظف', {
            'fields': ('status', 'termination_date', 'termination_reason')
        }),
        ('إعدادات النظام', {
            'fields': ('user', 'is_active', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'الاسم الكامل'


class EmployeeDocumentInline(admin.TabularInline):
    model = EmployeeDocument
    extra = 0
    fields = ['document_type', 'title', 'file', 'upload_date']
    readonly_fields = ['upload_date']


# إضافة الوثائق كـ inline للموظفين
EmployeeAdmin.inlines = [EmployeeDocumentInline]


@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'employee', 'document_type', 'upload_date']
    list_filter = ['document_type', 'upload_date']
    search_fields = ['title', 'employee__first_name', 'employee__last_name']
    autocomplete_fields = ['employee', 'uploaded_by']
