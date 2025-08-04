"""
HR Smart Core - Companies Models
نماذج إدارة الشركات والفروع
"""

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    """نموذج الشركة الأساسي"""
    
    name = models.CharField(
        max_length=200,
        verbose_name=_('اسم الشركة'),
        help_text=_('اسم الشركة كما هو مسجل رسمياً')
    )
    
    commercial_registration = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('السجل التجاري'),
        validators=[RegexValidator(
            regex=r'^\d{10}$',
            message=_('السجل التجاري يجب أن يكون 10 أرقام')
        )]
    )
    
    tax_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name=_('الرقم الضريبي'),
        validators=[RegexValidator(
            regex=r'^\d{15}$',
            message=_('الرقم الضريبي يجب أن يكون 15 رقم')
        )]
    )
    
    logo = models.ImageField(
        upload_to='companies/logos/',
        blank=True,
        null=True,
        verbose_name=_('شعار الشركة')
    )
    
    address = models.TextField(
        verbose_name=_('العنوان'),
        help_text=_('العنوان الكامل للشركة')
    )
    
    phone = models.CharField(
        max_length=20,
        verbose_name=_('رقم الهاتف'),
        validators=[RegexValidator(
            regex=r'^\+966[0-9]{9}$',
            message=_('رقم الهاتف يجب أن يبدأ بـ +966 ويتبعه 9 أرقام')
        )]
    )
    
    email = models.EmailField(
        verbose_name=_('البريد الإلكتروني')
    )
    
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('الموقع الإلكتروني')
    )
    
    # إعدادات مخصصة لكل شركة
    settings = models.JSONField(
        default=dict,
        verbose_name=_('إعدادات الشركة'),
        help_text=_('إعدادات مخصصة لكل شركة')
    )
    
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
        verbose_name = _('شركة')
        verbose_name_plural = _('الشركات')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_default_settings(self):
        """إعدادات افتراضية للشركة"""
        return {
            'work_hours_per_day': 8,
            'work_days_per_week': 6,
            'overtime_calculation': 'saudi_law',
            'leave_year_start': '01-01',
            'fiscal_year_start': '01-01',
            'currency': 'SAR',
            'location_tracking': True,
            'late_tolerance_minutes': 15,
        }


class Department(models.Model):
    """نموذج الأقسام"""
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='departments',
        verbose_name=_('الشركة')
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name=_('اسم القسم')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('وصف القسم')
    )
    
    manager = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments',
        verbose_name=_('مدير القسم')
    )
    
    parent_department = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sub_departments',
        verbose_name=_('القسم الرئيسي')
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('نشط')
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ الإنشاء')
    )
    
    class Meta:
        verbose_name = _('قسم')
        verbose_name_plural = _('الأقسام')
        unique_together = ['company', 'name']
        ordering = ['name']
    
    def __str__(self):
        return f"{self.company.name} - {self.name}"


class Position(models.Model):
    """نموذج المناصب الوظيفية"""
    
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name=_('القسم')
    )
    
    title = models.CharField(
        max_length=100,
        verbose_name=_('المسمى الوظيفي')
    )
    
    level = models.CharField(
        max_length=50,
        choices=[
            ('entry', _('مبتدئ')),
            ('junior', _('صغير')),
            ('senior', _('كبير')),
            ('lead', _('قائد')),
            ('manager', _('مدير')),
            ('director', _('مدير عام')),
        ],
        default='entry',
        verbose_name=_('المستوى')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('وصف المنصب')
    )
    
    requirements = models.TextField(
        blank=True,
        verbose_name=_('المتطلبات')
    )
    
    min_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('الحد الأدنى للراتب')
    )
    
    max_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('الحد الأعلى للراتب')
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('نشط')
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ الإنشاء')
    )
    
    class Meta:
        verbose_name = _('منصب وظيفي')
        verbose_name_plural = _('المناصب الوظيفية')
        unique_together = ['department', 'title']
        ordering = ['title']
    
    def __str__(self):
        return f"{self.department.name} - {self.title}"
