"""
HR Smart Core - Employees Models
نماذج إدارة الموظفين
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import date
import uuid


class Employee(models.Model):
    """نموذج الموظف الأساسي"""
    
    # رقم الموظف الفريد
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('رقم الموظف'),
        help_text=_('رقم تعريفي فريد للموظف')
    )
    
    # ربط بالمستخدم
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('حساب المستخدم')
    )
    
    # ربط بالشركة والقسم والمنصب
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name=_('الشركة')
    )
    
    department = models.ForeignKey(
        'companies.Department',
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees',
        verbose_name=_('القسم')
    )
    
    position = models.ForeignKey(
        'companies.Position',
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees',
        verbose_name=_('المنصب')
    )
    
    # البيانات الشخصية
    national_id = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_('رقم الهوية الوطنية'),
        validators=[RegexValidator(
            regex=r'^\d{10}$',
            message=_('رقم الهوية يجب أن يكون 10 أرقام')
        )]
    )
    
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('الاسم الأول')
    )
    
    last_name = models.CharField(
        max_length=100,
        verbose_name=_('اسم العائلة')
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name=_('البريد الإلكتروني')
    )
    
    phone = models.CharField(
        max_length=20,
        verbose_name=_('رقم الهاتف'),
        validators=[RegexValidator(
            regex=r'^\+966[0-9]{9}$',
            message=_('رقم الهاتف يجب أن يبدأ بـ +966 ويتبعه 9 أرقام')
        )]
    )
    
    birth_date = models.DateField(
        verbose_name=_('تاريخ الميلاد')
    )
    
    GENDER_CHOICES = [
        ('male', _('ذكر')),
        ('female', _('أنثى')),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name=_('الجنس')
    )
    
    nationality = models.CharField(
        max_length=50,
        default='سعودي',
        verbose_name=_('الجنسية')
    )
    
    address = models.TextField(
        verbose_name=_('العنوان')
    )
    
    # الصورة الشخصية
    profile_picture = models.ImageField(
        upload_to='employees/profiles/',
        blank=True,
        null=True,
        verbose_name=_('الصورة الشخصية')
    )
    
    # البيانات الوظيفية
    hire_date = models.DateField(
        verbose_name=_('تاريخ التوظيف')
    )
    
    CONTRACT_TYPES = [
        ('permanent', _('دائم')),
        ('temporary', _('مؤقت')),
        ('contract', _('تعاقد')),
        ('part_time', _('دوام جزئي')),
    ]
    contract_type = models.CharField(
        max_length=20,
        choices=CONTRACT_TYPES,
        default='permanent',
        verbose_name=_('نوع العقد')
    )
    
    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('الراتب الأساسي')
    )
    
    work_hours_per_day = models.IntegerField(
        default=8,
        verbose_name=_('ساعات العمل اليومية')
    )
    
    work_days_per_week = models.IntegerField(
        default=6,
        verbose_name=_('أيام العمل الأسبوعية')
    )
    
    # بيانات المدير المباشر
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name=_('المدير المباشر')
    )
    
    # حالة الموظف
    STATUS_CHOICES = [
        ('active', _('نشط')),
        ('suspended', _('موقوف')),
        ('terminated', _('منتهي الخدمة')),
        ('on_leave', _('في إجازة')),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name=_('حالة الموظف')
    )
    
    termination_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ انتهاء الخدمة')
    )
    
    termination_reason = models.TextField(
        blank=True,
        verbose_name=_('سبب انتهاء الخدمة')
    )
    
    # معلومات إضافية
    emergency_contact_name = models.CharField(
        max_length=100,
        verbose_name=_('اسم جهة الاتصال للطوارئ')
    )
    
    emergency_contact_phone = models.CharField(
        max_length=20,
        verbose_name=_('رقم هاتف الطوارئ')
    )
    
    emergency_contact_relation = models.CharField(
        max_length=50,
        verbose_name=_('صلة القرابة')
    )
    
    # بيانات النظام
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('نشط')
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ الإنشاء')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('تاريخ التحديث')
    )
    
    class Meta:
        verbose_name = _('موظف')
        verbose_name_plural = _('الموظفين')
        ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.employee_id} - {self.get_full_name()}"
    
    def get_full_name(self):
        """الحصول على الاسم الكامل"""
        return f"{self.first_name} {self.last_name}"
    
    def get_years_of_service(self):
        """حساب سنوات الخدمة"""
        if self.termination_date:
            end_date = self.termination_date
        else:
            end_date = date.today()
        
        years = (end_date - self.hire_date).days / 365.25
        return round(years, 2)
    
    def get_monthly_salary(self):
        """الحصول على الراتب الشهري الإجمالي"""
        # سيتم تطويره في تطبيق الرواتب
        return self.basic_salary
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            # إنشاء رقم موظف تلقائي
            company_code = self.company.commercial_registration[-3:]
            year = timezone.now().year
            # البحث عن آخر رقم موظف
            last_employee = Employee.objects.filter(
                company=self.company,
                employee_id__startswith=f"{company_code}{year}"
            ).order_by('employee_id').last()
            
            if last_employee:
                last_number = int(last_employee.employee_id[-4:])
                new_number = last_number + 1
            else:
                new_number = 1
            
            self.employee_id = f"{company_code}{year}{new_number:04d}"
        
        super().save(*args, **kwargs)


class EmployeeDocument(models.Model):
    """نموذج وثائق الموظف"""
    
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name=_('الموظف')
    )
    
    DOCUMENT_TYPES = [
        ('id_copy', _('صورة الهوية')),
        ('passport', _('جواز السفر')),
        ('contract', _('العقد')),
        ('certificate', _('الشهادة')),
        ('medical_report', _('التقرير الطبي')),
        ('bank_account', _('كشف حساب بنكي')),
        ('other', _('أخرى')),
    ]
    
    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES,
        verbose_name=_('نوع الوثيقة')
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name=_('عنوان الوثيقة')
    )
    
    file = models.FileField(
        upload_to='employees/documents/',
        verbose_name=_('الملف')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('الوصف')
    )
    
    upload_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ الرفع')
    )
    
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('رفع بواسطة')
    )
    
    class Meta:
        verbose_name = _('وثيقة موظف')
        verbose_name_plural = _('وثائق الموظفين')
        ordering = ['-upload_date']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.title}"
