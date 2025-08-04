"""
HR Smart Core - Authentication Models
نماذج المصادقة والصلاحيات
"""

from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    """نموذج ملف المستخدم الإضافي"""
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('المستخدم')
    )
    
    # معلومات إضافية
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('رقم الهاتف')
    )
    
    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True,
        null=True,
        verbose_name=_('الصورة الشخصية')
    )
    
    # إعدادات النظام
    language = models.CharField(
        max_length=10,
        choices=[
            ('ar', _('العربية')),
            ('en', _('English')),
        ],
        default='ar',
        verbose_name=_('اللغة')
    )
    
    timezone = models.CharField(
        max_length=50,
        default='Asia/Riyadh',
        verbose_name=_('المنطقة الزمنية')
    )
    
    # معلومات الجلسات
    last_activity = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('آخر نشاط')
    )
    
    failed_login_attempts = models.IntegerField(
        default=0,
        verbose_name=_('محاولات تسجيل الدخول الفاشلة')
    )
    
    is_locked = models.BooleanField(
        default=False,
        verbose_name=_('محظور')
    )
    
    locked_until = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('محظور حتى')
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
        verbose_name = _('ملف المستخدم')
        verbose_name_plural = _('ملفات المستخدمين')
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"


class Role(models.Model):
    """نموذج الأدوار"""
    
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('اسم الدور')
    )
    
    description = models.TextField(
        blank=True,
        verbose_name=_('الوصف')
    )
    
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        verbose_name=_('الصلاحيات')
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
        verbose_name = _('دور')
        verbose_name_plural = _('الأدوار')
        ordering = ['name']
    
    def __str__(self):
        return self.name


class UserRole(models.Model):
    """نموذج ربط المستخدمين بالأدوار"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name=_('المستخدم')
    )
    
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name=_('الدور')
    )
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name=_('الشركة')
    )
    
    granted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='granted_roles',
        verbose_name=_('منح بواسطة')
    )
    
    granted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('تاريخ المنح')
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('نشط')
    )
    
    class Meta:
        verbose_name = _('دور المستخدم')
        verbose_name_plural = _('أدوار المستخدمين')
        unique_together = ['user', 'role', 'company']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role.name} - {self.company.name}"


class LoginLog(models.Model):
    """نموذج سجل تسجيل الدخول"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='login_logs',
        verbose_name=_('المستخدم')
    )
    
    ip_address = models.GenericIPAddressField(
        verbose_name=_('عنوان IP')
    )
    
    user_agent = models.TextField(
        verbose_name=_('متصفح المستخدم')
    )
    
    login_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('وقت تسجيل الدخول')
    )
    
    logout_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('وقت تسجيل الخروج')
    )
    
    is_successful = models.BooleanField(
        default=True,
        verbose_name=_('نجح تسجيل الدخول')
    )
    
    failure_reason = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('سبب الفشل')
    )
    
    class Meta:
        verbose_name = _('سجل تسجيل الدخول')
        verbose_name_plural = _('سجلات تسجيل الدخول')
        ordering = ['-login_time']
    
    def __str__(self):
        return f"{self.user.username} - {self.login_time}"
