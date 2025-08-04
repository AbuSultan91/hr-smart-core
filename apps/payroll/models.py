"""
HR Smart Core - Payroll Models
نماذج نظام الرواتب
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from decimal import Decimal


class SalaryComponent(models.Model):
    """نموذج مكونات الراتب"""
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='salary_components',
        verbose_name=_('الشركة')
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name=_('اسم المكون')
    )
    
    COMPONENT_TYPES = [
        ('allowance', _('بدل')),
        ('deduction', _('خصم')),
        ('bonus', _('مكافأة')),
        ('overtime', _('إضافي')),
    ]
    
    component_type = models.CharField(
        max_length=20,
        choices=COMPONENT_TYPES,
        verbose_name=_('نوع المكون')
    )
    
    CALCULATION_TYPES = [
        ('fixed', _('مبلغ ثابت')),
        ('percentage', _('نسبة مئوية')),
        ('formula', _('معادلة حسابية')),
    ]
    
    calculation_type = models.CharField(
        max_length=20,
        choices=CALCULATION_TYPES,
        verbose_name=_('طريقة الحساب')
    )
    
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('القيمة')
    )
    
    formula = models.TextField(
        blank=True,
        verbose_name=_('المعادلة الحسابية'),
        help_text=_('للاستخدام مع طريقة الحساب بالمعادلة')
    )
    
    is_taxable = models.BooleanField(
        default=True,
        verbose_name=_('خاضع للضريبة')
    )
    
    affects_overtime = models.BooleanField(
        default=False,
        verbose_name=_('يؤثر على حساب الإضافي')
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('نشط')
    )
    
    class Meta:
        verbose_name = _('مكون راتب')
        verbose_name_plural = _('مكونات الراتب')
        unique_together = ['company', 'name']
    
    def __str__(self):
        return f"{self.company.name} - {self.name}"


class EmployeeSalary(models.Model):
    """نموذج راتب الموظف"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='salary_records',
        verbose_name=_('الموظف')
    )
    
    effective_date = models.DateField(
        verbose_name=_('ساري من')
    )
    
    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('الراتب الأساسي')
    )
    
    # البدلات الثابتة
    housing_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل السكن')
    )
    
    transport_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل المواصلات')
    )
    
    food_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل الطعام')
    )
    
    # مكونات أخرى
    other_allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدلات أخرى')
    )
    
    # معلومات التأمين
    insurance_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('9.00'),
        verbose_name=_('نسبة التأمين %')
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
        verbose_name = _('راتب موظف')
        verbose_name_plural = _('رواتب الموظفين')
        ordering = ['-effective_date']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.effective_date}"
    
    @property
    def total_allowances(self):
        """إجمالي البدلات"""
        return (self.housing_allowance + self.transport_allowance + 
                self.food_allowance + self.other_allowances)
    
    @property
    def gross_salary(self):
        """الراتب الإجمالي"""
        return self.basic_salary + self.total_allowances
    
    @property
    def insurance_deduction(self):
        """خصم التأمين"""
        return (self.basic_salary * self.insurance_percentage) / 100


class Payroll(models.Model):
    """نموذج كشف الراتب الشهري"""
    
    employee = models.ForeignKey(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='payrolls',
        verbose_name=_('الموظف')
    )
    
    month = models.IntegerField(
        verbose_name=_('الشهر')
    )
    
    year = models.IntegerField(
        verbose_name=_('السنة')
    )
    
    # الراتب الأساسي والبدلات
    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('الراتب الأساسي')
    )
    
    housing_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل السكن')
    )
    
    transport_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل المواصلات')
    )
    
    food_allowance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدل الطعام')
    )
    
    overtime_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('مبلغ الإضافي')
    )
    
    bonus_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('المكافآت')
    )
    
    other_allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('بدلات أخرى')
    )
    
    # الخصومات
    insurance_deduction = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصم التأمين')
    )
    
    absence_deduction = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصم الغياب')
    )
    
    late_deduction = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصم التأخير')
    )
    
    other_deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('خصومات أخرى')
    )
    
    # الإجماليات
    gross_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('الراتب الإجمالي')
    )
    
    total_deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('إجمالي الخصومات')
    )
    
    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('صافي الراتب')
    )
    
    # معلومات الحضور
    working_days = models.IntegerField(
        default=0,
        verbose_name=_('أيام العمل')
    )
    
    present_days = models.IntegerField(
        default=0,
        verbose_name=_('أيام الحضور')
    )
    
    absent_days = models.IntegerField(
        default=0,
        verbose_name=_('أيام الغياب')
    )
    
    overtime_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('ساعات الإضافي')
    )
    
    # حالة كشف الراتب
    STATUS_CHOICES = [
        ('draft', _('مسودة')),
        ('calculated', _('محسوب')),
        ('approved', _('معتمد')),
        ('paid', _('مدفوع')),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name=_('الحالة')
    )
    
    # معلومات الاعتماد والدفع
    approved_by = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_payrolls',
        verbose_name=_('اعتمد بواسطة')
    )
    
    approved_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ الاعتماد')
    )
    
    payment_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ الدفع')
    )
    
    notes = models.TextField(
        blank=True,
        verbose_name=_('ملاحظات')
    )
    
    # تواريخ النظام
    generated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ الإنشاء')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('تاريخ التحديث')
    )
    
    class Meta:
        verbose_name = _('كشف راتب')
        verbose_name_plural = _('كشوف الرواتب')
        unique_together = ['employee', 'month', 'year']
        ordering = ['-year', '-month', 'employee']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.month}/{self.year}"
    
    def calculate_totals(self):
        """حساب الإجماليات"""
        self.gross_salary = (
            self.basic_salary + self.housing_allowance + 
            self.transport_allowance + self.food_allowance +
            self.overtime_amount + self.bonus_amount + self.other_allowances
        )
        
        self.total_deductions = (
            self.insurance_deduction + self.absence_deduction +
            self.late_deduction + self.other_deductions
        )
        
        self.net_salary = self.gross_salary - self.total_deductions
    
    def save(self, *args, **kwargs):
        self.calculate_totals()
        super().save(*args, **kwargs)


class EndOfServiceBenefit(models.Model):
    """نموذج مكافأة نهاية الخدمة"""
    
    employee = models.OneToOneField(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='end_of_service_benefit',
        verbose_name=_('الموظف')
    )
    
    service_years = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('سنوات الخدمة')
    )
    
    last_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('آخر راتب')
    )
    
    calculated_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('المبلغ المحسوب')
    )
    
    REASON_CHOICES = [
        ('resignation', _('استقالة')),
        ('termination', _('فصل')),
        ('retirement', _('تقاعد')),
        ('death', _('وفاة')),
    ]
    
    termination_reason = models.CharField(
        max_length=20,
        choices=REASON_CHOICES,
        verbose_name=_('سبب انتهاء الخدمة')
    )
    
    calculation_date = models.DateField(
        verbose_name=_('تاريخ الحساب')
    )
    
    is_paid = models.BooleanField(
        default=False,
        verbose_name=_('مدفوع')
    )
    
    payment_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('تاريخ الدفع')
    )
    
    notes = models.TextField(
        blank=True,
        verbose_name=_('ملاحظات')
    )
    
    class Meta:
        verbose_name = _('مكافأة نهاية الخدمة')
        verbose_name_plural = _('مكافآت نهاية الخدمة')
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.calculated_amount}"
    
    def calculate_benefit(self):
        """حساب مكافأة نهاية الخدمة حسب النظام السعودي"""
        # حساب مكافأة نهاية الخدمة وفقاً لنظام العمل السعودي
        if self.service_years < 2:
            # أقل من سنتين - لا يستحق مكافأة
            benefit = Decimal('0.00')
        elif self.service_years < 5:
            # من سنتين إلى 5 سنوات - نصف راتب شهر عن كل سنة
            benefit = (self.last_salary / 2) * self.service_years
        elif self.service_years < 10:
            # من 5 إلى 10 سنوات - نصف راتب عن أول 5 سنوات + راتب كامل عن الباقي
            first_5_years = (self.last_salary / 2) * 5
            remaining_years = self.service_years - 5
            remaining_benefit = self.last_salary * remaining_years
            benefit = first_5_years + remaining_benefit
        else:
            # أكثر من 10 سنوات - راتب شهر عن كل سنة (حد أقصى 24 شهر)
            max_months = min(24, self.service_years)
            benefit = self.last_salary * max_months
        
        # تطبيق قواعد خاصة حسب سبب انتهاء الخدمة
        if self.termination_reason == 'resignation' and self.service_years < 5:
            # في حالة الاستقالة قبل 5 سنوات، يحصل على ثلث المكافأة فقط
            benefit = benefit / 3
        elif self.termination_reason == 'termination':
            # في حالة الفصل، قد لا يحصل على شيء أو جزء حسب السبب
            benefit = benefit / 2  # يمكن تخصيص هذا حسب سياسة الشركة
        
        return benefit
    
    def save(self, *args, **kwargs):
        if not self.calculated_amount:
            self.calculated_amount = self.calculate_benefit()
        super().save(*args, **kwargs)
