"""
HR Smart Core - Attendance Models
نماذج نظام الحضور والانصراف
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from datetime import datetime, time


class AttendanceRecord(models.Model):
    """نموذج تسجيل الحضور والانصراف"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name=_('الموظف')
    )
    
    date = models.DateField(
        verbose_name=_('التاريخ')
    )
    
    # أوقات الحضور والانصراف
    check_in_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('وقت الحضور')
    )
    
    check_out_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('وقت الانصراف')
    )
    
    # أوقات الاستراحة
    break_start_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('بداية الاستراحة')
    )
    
    break_end_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('نهاية الاستراحة')
    )
    
    # الموقع الجغرافي
    check_in_location_lat = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=True,
        blank=True,
        verbose_name=_('خط العرض للحضور')
    )
    
    check_in_location_lng = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True,
        verbose_name=_('خط الطول للحضور')
    )
    
    check_out_location_lat = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=True,
        blank=True,
        verbose_name=_('خط العرض للانصراف')
    )
    
    check_out_location_lng = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True,
        verbose_name=_('خط الطول للانصراف')
    )
    
    # الحسابات
    work_hours = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('ساعات العمل')
    )
    
    overtime_hours = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('الساعات الإضافية')
    )
    
    late_minutes = models.IntegerField(
        default=0,
        verbose_name=_('دقائق التأخير')
    )
    
    early_leave_minutes = models.IntegerField(
        default=0,
        verbose_name=_('دقائق المغادرة المبكرة')
    )
    
    break_minutes = models.IntegerField(
        default=0,
        verbose_name=_('دقائق الاستراحة')
    )
    
    # الحالة
    STATUS_CHOICES = [
        ('present', _('حاضر')),
        ('absent', _('غائب')),
        ('late', _('متأخر')),
        ('early_leave', _('مغادرة مبكرة')),
        ('partial', _('حضور جزئي')),
        ('holiday', _('عطلة')),
        ('leave', _('إجازة')),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='present',
        verbose_name=_('الحالة')
    )
    
    notes = models.TextField(
        blank=True,
        verbose_name=_('ملاحظات')
    )
    
    # معلومات إضافية
    is_manual_entry = models.BooleanField(
        default=False,
        verbose_name=_('إدخال يدوي')
    )
    
    manual_entry_reason = models.TextField(
        blank=True,
        verbose_name=_('سبب الإدخال اليدوي')
    )
    
    approved_by = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_attendance',
        verbose_name=_('وافق عليه')
    )
    
    approved_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ الموافقة')
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
        verbose_name = _('سجل حضور')
        verbose_name_plural = _('سجلات الحضور')
        unique_together = ['employee', 'date']
        ordering = ['-date', 'employee']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.date}"
    
    def calculate_work_hours(self):
        """حساب ساعات العمل"""
        if not self.check_in_time or not self.check_out_time:
            return Decimal('0.00')
        
        # تحويل الأوقات إلى دقائق
        check_in_minutes = self.check_in_time.hour * 60 + self.check_in_time.minute
        check_out_minutes = self.check_out_time.hour * 60 + self.check_out_time.minute
        
        # حساب إجمالي الدقائق
        total_minutes = check_out_minutes - check_in_minutes
        
        # خصم فترة الاستراحة
        if self.break_start_time and self.break_end_time:
            break_start_minutes = self.break_start_time.hour * 60 + self.break_start_time.minute
            break_end_minutes = self.break_end_time.hour * 60 + self.break_end_time.minute
            break_duration = break_end_minutes - break_start_minutes
            total_minutes -= break_duration
            self.break_minutes = break_duration
        
        # تحويل إلى ساعات
        work_hours = Decimal(str(total_minutes / 60))
        return round(work_hours, 2)
    
    def calculate_overtime(self):
        """حساب الساعات الإضافية"""
        standard_hours = Decimal(str(self.employee.work_hours_per_day))
        actual_hours = self.calculate_work_hours()
        
        if actual_hours > standard_hours:
            return actual_hours - standard_hours
        return Decimal('0.00')
    
    def calculate_late_minutes(self):
        """حساب دقائق التأخير"""
        if not self.check_in_time:
            return 0
        
        # وقت بداية العمل الرسمي (افتراضي 8:00 صباحاً)
        standard_start_time = time(8, 0)
        
        if self.check_in_time > standard_start_time:
            late_delta = datetime.combine(self.date, self.check_in_time) - \
                        datetime.combine(self.date, standard_start_time)
            return int(late_delta.total_seconds() / 60)
        return 0
    
    def save(self, *args, **kwargs):
        # حساب الساعات والدقائق تلقائياً
        self.work_hours = self.calculate_work_hours()
        self.overtime_hours = self.calculate_overtime()
        self.late_minutes = self.calculate_late_minutes()
        
        # تحديد الحالة
        if not self.check_in_time and not self.check_out_time:
            self.status = 'absent'
        elif self.late_minutes > 0:
            self.status = 'late'
        elif self.early_leave_minutes > 0:
            self.status = 'early_leave'
        else:
            self.status = 'present'
        
        super().save(*args, **kwargs)


class WorkSchedule(models.Model):
    """نموذج جدولة العمل"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='work_schedules',
        verbose_name=_('الموظف')
    )
    
    WEEKDAY_CHOICES = [
        (0, _('الاثنين')),
        (1, _('الثلاثاء')),
        (2, _('الأربعاء')),
        (3, _('الخميس')),
        (4, _('الجمعة')),
        (5, _('السبت')),
        (6, _('الأحد')),
    ]
    
    weekday = models.IntegerField(
        choices=WEEKDAY_CHOICES,
        verbose_name=_('يوم الأسبوع')
    )
    
    start_time = models.TimeField(
        verbose_name=_('وقت البداية')
    )
    
    end_time = models.TimeField(
        verbose_name=_('وقت النهاية')
    )
    
    break_start_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('بداية الاستراحة')
    )
    
    break_end_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('نهاية الاستراحة')
    )
    
    is_working_day = models.BooleanField(
        default=True,
        verbose_name=_('يوم عمل')
    )
    
    effective_from = models.DateField(
        verbose_name=_('ساري من')
    )
    
    effective_to = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('ساري حتى')
    )
    
    class Meta:
        verbose_name = _('جدولة عمل')
        verbose_name_plural = _('جدولة العمل')
        unique_together = ['employee', 'weekday', 'effective_from']
        ordering = ['employee', 'weekday']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.get_weekday_display()}"


class AttendancePolicy(models.Model):
    """نموذج سياسة الحضور"""
    
    company = models.OneToOneField(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='attendance_policy',
        verbose_name=_('الشركة')
    )
    
    # سياسة التأخير
    late_tolerance_minutes = models.IntegerField(
        default=15,
        verbose_name=_('الحد المسموح للتأخير (دقيقة)')
    )
    
    late_deduction_per_minute = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصم لكل دقيقة تأخير')
    )
    
    # سياسة الغياب
    absence_deduction_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصم يوم الغياب')
    )
    
    # سياسة الساعات الإضافية
    overtime_rate_weekday = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('1.50'),
        verbose_name=_('معدل الإضافي في أيام العمل')
    )
    
    overtime_rate_weekend = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('2.00'),
        verbose_name=_('معدل الإضافي في العطل')
    )
    
    # إعدادات عامة
    require_location_tracking = models.BooleanField(
        default=True,
        verbose_name=_('تتبع الموقع مطلوب')
    )
    
    allowed_distance_meters = models.IntegerField(
        default=100,
        verbose_name=_('المسافة المسموحة بالمتر')
    )
    
    auto_checkout_hours = models.IntegerField(
        default=12,
        verbose_name=_('انصراف تلقائي بعد (ساعة)')
    )
    
    class Meta:
        verbose_name = _('سياسة الحضور')
        verbose_name_plural = _('سياسات الحضور')
    
    def __str__(self):
        return f"سياسة حضور {self.company.name}"
