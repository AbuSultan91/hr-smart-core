"""
HR Smart Core - Leaves Models
نماذج نظام الإجازات
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import date, timedelta


class LeaveType(models.Model):
    """نموذج أنواع الإجازات"""
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='leave_types',
        verbose_name=_('الشركة')
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name=_('نوع الإجازة')
    )
    
    LEAVE_CATEGORIES = [
        ('annual', _('إجازة سنوية')),
        ('sick', _('إجازة مرضية')),
        ('maternity', _('إجازة وضع')),
        ('paternity', _('إجازة والدية')),
        ('hajj', _('إجازة حج')),
        ('emergency', _('إجازة طارئة')),
        ('study', _('إجازة دراسية')),
        ('unpaid', _('إجازة بدون راتب')),
        ('compensatory', _('إجازة تعويضية')),
        ('other', _('أخرى')),
    ]
    
    category = models.CharField(
        max_length=20,
        choices=LEAVE_CATEGORIES,
        verbose_name=_('الفئة')
    )
    
    max_days_per_year = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_('الحد الأقصى في السنة')
    )
    
    max_consecutive_days = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('الحد الأقصى المتتالي')
    )
    
    is_paid = models.BooleanField(
        default=True,
        verbose_name=_('مدفوعة الراتب')
    )
    
    carry_forward = models.BooleanField(
        default=False,
        verbose_name=_('قابلة للترحيل')
    )
    
    max_carry_forward_days = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('الحد الأقصى للترحيل')
    )
    
    requires_medical_certificate = models.BooleanField(
        default=False,
        verbose_name=_('تتطلب شهادة طبية')
    )
    
    advance_notice_days = models.IntegerField(
        default=3,
        verbose_name=_('فترة الإشعار المسبق (أيام)')
    )
    
    # قوانين خاصة بالجنس
    gender_specific = models.CharField(
        max_length=10,
        choices=[
            ('both', _('كلا الجنسين')),
            ('male', _('ذكور فقط')),
            ('female', _('إناث فقط')),
        ],
        default='both',
        verbose_name=_('خاص بالجنس')
    )
    
    # شروط الاستحقاق
    minimum_service_months = models.IntegerField(
        default=0,
        verbose_name=_('الحد الأدنى لفترة الخدمة (شهر)')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('الوصف')
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
        verbose_name = _('نوع إجازة')
        verbose_name_plural = _('أنواع الإجازات')
        unique_together = ['company', 'name']
        ordering = ['name']
    
    def __str__(self):
        return f"{self.company.name} - {self.name}"


class LeaveBalance(models.Model):
    """نموذج رصيد الإجازات"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='leave_balances',
        verbose_name=_('الموظف')
    )
    
    leave_type = models.ForeignKey(
        LeaveType,
        on_delete=models.CASCADE,
        related_name='balances',
        verbose_name=_('نوع الإجازة')
    )
    
    year = models.IntegerField(
        verbose_name=_('السنة')
    )
    
    entitled_days = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('الأيام المستحقة')
    )
    
    used_days = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('الأيام المستخدمة')
    )
    
    carried_forward_days = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('الأيام المرحلة')
    )
    
    class Meta:
        verbose_name = _('رصيد إجازة')
        verbose_name_plural = _('أرصدة الإجازات')
        unique_together = ['employee', 'leave_type', 'year']
        ordering = ['-year', 'employee']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.leave_type.name} - {self.year}"
    
    @property
    def remaining_days(self):
        """الأيام المتبقية"""
        return self.entitled_days + self.carried_forward_days - self.used_days


class LeaveRequest(models.Model):
    """نموذج طلب الإجازة"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='leave_requests',
        verbose_name=_('الموظف')
    )
    
    leave_type = models.ForeignKey(
        LeaveType,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name=_('نوع الإجازة')
    )
    
    start_date = models.DateField(
        verbose_name=_('تاريخ البداية')
    )
    
    end_date = models.DateField(
        verbose_name=_('تاريخ النهاية')
    )
    
    days_count = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('عدد الأيام')
    )
    
    reason = models.TextField(
        verbose_name=_('السبب')
    )
    
    # معلومات الاتصال أثناء الإجازة
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('رقم الاتصال')
    )
    
    contact_address = models.TextField(
        blank=True,
        verbose_name=_('عنوان الاتصال')
    )
    
    # المرفقات
    attachment = models.FileField(
        upload_to='leaves/attachments/',
        blank=True,
        null=True,
        verbose_name=_('مرفق')
    )
    
    # تفويض المهام
    delegate_to = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='delegated_tasks',
        verbose_name=_('تفويض المهام إلى')
    )
    
    # حالة الطلب
    STATUS_CHOICES = [
        ('pending', _('قيد المراجعة')),
        ('approved', _('موافق عليه')),
        ('rejected', _('مرفوض')),
        ('cancelled', _('ملغي')),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_('الحالة')
    )
    
    # معلومات الموافقة/الرفض
    reviewed_by = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_leaves',
        verbose_name=_('راجع بواسطة')
    )
    
    reviewed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ المراجعة')
    )
    
    review_notes = models.TextField(
        blank=True,
        verbose_name=_('ملاحظات المراجعة')
    )
    
    # تواريخ النظام
    applied_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ التقديم')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('تاريخ التحديث')
    )
    
    class Meta:
        verbose_name = _('طلب إجازة')
        verbose_name_plural = _('طلبات الإجازات')
        ordering = ['-applied_at']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.leave_type.name} - {self.start_date}"
    
    def calculate_days(self):
        """حساب عدد أيام الإجازة"""
        if self.start_date and self.end_date:
            # حساب الأيام مع استثناء أيام العطل
            total_days = (self.end_date - self.start_date).days + 1
            
            # يمكن تطوير هذا لاستثناء أيام الجمعة والعطل الرسمية
            # حالياً سنحسب جميع الأيام
            return Decimal(str(total_days))
        return Decimal('0.00')
    
    def save(self, *args, **kwargs):
        if not self.days_count:
            self.days_count = self.calculate_days()
        super().save(*args, **kwargs)
    
    def can_approve(self):
        """فحص إمكانية الموافقة على الطلب"""
        if self.status != 'pending':
            return False, _('الطلب تم مراجعته مسبقاً')
        
        # فحص الرصيد المتاح
        try:
            balance = LeaveBalance.objects.get(
                employee=self.employee,
                leave_type=self.leave_type,
                year=self.start_date.year
            )
            if balance.remaining_days < self.days_count:
                return False, _('الرصيد غير كافي')
        except LeaveBalance.DoesNotExist:
            return False, _('لا يوجد رصيد لهذا النوع من الإجازات')
        
        # فحص فترة الإشعار المسبق
        notice_days = (self.start_date - date.today()).days
        if notice_days < self.leave_type.advance_notice_days:
            return False, f"يجب تقديم الطلب قبل {self.leave_type.advance_notice_days} أيام على الأقل"
        
        return True, _('يمكن الموافقة على الطلب')


class Holiday(models.Model):
    """نموذج العطل الرسمية"""
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='holidays',
        verbose_name=_('الشركة')
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name=_('اسم العطلة')
    )
    
    date = models.DateField(
        verbose_name=_('التاريخ')
    )
    
    HOLIDAY_TYPES = [
        ('national', _('عطلة وطنية')),
        ('religious', _('عطلة دينية')),
        ('company', _('عطلة الشركة')),
    ]
    
    holiday_type = models.CharField(
        max_length=20,
        choices=HOLIDAY_TYPES,
        default='national',
        verbose_name=_('نوع العطلة')
    )
    
    is_recurring = models.BooleanField(
        default=False,
        verbose_name=_('عطلة متكررة سنوياً')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('الوصف')
    )
    
    class Meta:
        verbose_name = _('عطلة رسمية')
        verbose_name_plural = _('العطل الرسمية')
        unique_together = ['company', 'date']
        ordering = ['date']
    
    def __str__(self):
        return f"{self.name} - {self.date}"
