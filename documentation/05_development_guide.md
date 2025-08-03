# 💻 دليل المطور الشامل

**تاريخ الإنشاء**: 3 أغسطس 2025  
**آخر تحديث**: 3 أغسطس 2025  
**الإصدار**: 1.0.0

---

## 🎯 منهجية التطوير

### مبادئ التطوير الأساسية:

1. **الاختبار أولاً (Test-First Development)**
   - إنشاء ملف اختبار لكل وظيفة جديدة
   - اختبار النجاح قبل التطبيق في المشروع الفعلي
   - حذف ملفات الاختبار بعد النجاح للحفاظ على نظافة الهيكل

2. **فصل الاهتمامات (Separation of Concerns)**
   - فصل الكود البرمجي عن التصميم والستايل
   - استخدام ملفات منفصلة للـ CSS و JavaScript
   - منطق العمل منفصل عن واجهة المستخدم

3. **نظام تحليل الأخطاء**
   - زر مدمج لتحليل وإصلاح الأخطاء
   - تسجيل جميع الأخطاء مع تفاصيل واضحة
   - اقتراح حلول تلقائية للأخطاء الشائعة

---

## 📚 قائمة التطبيقات والمكتبات الكاملة

### التطبيقات الأساسية:

#### 1. 🔐 Authentication (المصادقة)
- **الغرض**: إدارة تسجيل الدخول والصلاحيات
- **المكتبات**: Django Auth, JWT للـ API
- **الملفات الرئيسية**:
  - `models.py`: نماذج المستخدمين المخصصة
  - `views.py`: عمليات تسجيل الدخول والخروج
  - `permissions.py`: صلاحيات مخصصة
  - `decorators.py`: ديكوريتورز للحماية

#### 2. 🏢 Companies (الشركات)
- **الغرض**: إدارة الشركات المتعددة
- **المكتبات**: Django ORM, Pillow للشعارات
- **الملفات الرئيسية**:
  - `models.py`: نماذج الشركات والفروع
  - `views.py`: إدارة بيانات الشركات
  - `tenant_utils.py`: أدوات multi-tenant

#### 3. 👥 Employees (الموظفين)
- **الغرض**: إدارة بيانات الموظفين
- **المكتبات**: Django Forms, Pillow للصور
- **الملفات الرئيسية**:
  - `models.py`: نماذج الموظفين والأقسام
  - `views.py`: عمليات CRUD للموظفين
  - `signals.py`: إنشاء حسابات تلقائية

#### 4. ⏰ Attendance (الحضور)
- **الغرض**: تتبع الحضور والانصراف
- **المكتبات**: GeoDjango للمواقع, Celery للمهام
- **الملفات الرئيسية**:
  - `models.py`: نماذج سجلات الحضور
  - `api_views.py`: APIs للتطبيق المحمول
  - `location_utils.py`: التحقق من الموقع

#### 5. 🏖 Leaves (الإجازات)
- **الغرض**: إدارة طلبات الإجازات
- **المكتبات**: Django Workflow, python-dateutil
- **الملفات الرئيسية**:
  - `models.py`: أنواع وطلبات الإجازات
  - `calculations.py`: حسابات الأرصدة
  - `workflows.py`: سير عمل الموافقات

#### 6. 💰 Payroll (الرواتب)
- **الغرض**: حساب وإدارة الرواتب
- **المكتبات**: Decimal للحسابات الدقيقة
- **الملفات الرئيسية**:
  - `models.py`: نماذج الرواتب والبدلات
  - `calculations.py`: حسابات معقدة
  - `saudi_rules.py`: قوانين العمل السعودية

#### 7. 📊 Reports (التقارير)
- **الغرض**: إنشاء وتصدير التقارير
- **المكتبات**: ReportLab, openpyxl, Chart.js
- **الملفات الرئيسية**:
  - `generators.py`: مولدات التقارير
  - `exporters.py`: تصدير PDF/Excel
  - `chart_utils.py`: الرسوم البيانية

### التطبيقات الإضافية:

#### 8. 🎓 Training (التدريب)
- **الغرض**: إدارة برامج التدريب والتطوير
- **المكتبات**: Django Forms, Calendar
- **الملفات الرئيسية**:
  - `models.py`: الدورات والشهادات
  - `views.py`: تسجيل ومتابعة التدريب

#### 9. 📈 Performance (الأداء)
- **الغرض**: تقييم أداء الموظفين
- **المكتبات**: Django Forms, Chart.js
- **الملفات الرئيسية**:
  - `models.py`: نماذج التقييم
  - `views.py`: عمليات التقييم

#### 10. 📝 Complaints (الشكاوى)
- **الغرض**: إدارة الشكاوى والمقترحات
- **المكتبات**: Django Messages
- **الملفات الرئيسية**:
  - `models.py`: نماذج الشكاوى
  - `workflows.py`: سير عمل المعالجة

#### 11. 📅 Meetings (الاجتماعات)
- **الغرض**: جدولة ومتابعة الاجتماعات
- **المكتبات**: Django Calendar, FullCalendar.js
- **الملفات الرئيسية**:
  - `models.py`: نماذج الاجتماعات
  - `calendar_utils.py`: أدوات التقويم

#### 12. 🏢 Assets (الأصول)
- **الغرض**: إدارة أصول ومعدات الشركة
- **المكتبات**: Django Forms, QR Code
- **الملفات الرئيسية**:
  - `models.py`: نماذج الأصول
  - `tracking_utils.py`: تتبع الأصول

#### 13. 🔔 Notifications (الإشعارات)
- **الغرض**: نظام إشعارات شامل
- **المكتبات**: Django Channels, WebSockets
- **الملفات الرئيسية**:
  - `models.py`: نماذج الإشعارات
  - `utils.py`: إرسال الإشعارات

#### 14. 🔧 System (النظام)
- **الغرض**: إدارة النظام وتحليل الأخطاء
- **المكتبات**: Django Logging, psutil
- **الملفات الرئيسية**:
  - `error_analyzer.py`: تحليل الأخطاء
  - `system_monitor.py`: مراقبة النظام

---

## 🛠 خطوات العمل التفصيلية

### المرحلة 1: التطبيقات الأساسية (4-6 أسابيع)

#### الأسبوع 1-2: نظام المصادقة والشركات
```python
# خطوات العمل:
# 1. إنشاء ملف اختبار
touch tests/test_authentication.py

# 2. كتابة اختبار أساسي
# tests/test_authentication.py
import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from apps.authentication.models import UserProfile

class AuthTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username='1234',  # آخر 4 أرقام من الهوية
            password='1234',  # أول 4 أرقام من الهوية
            email='test@example.com'
        )
        self.assertTrue(user.is_active)
        self.assertEqual(user.username, '1234')

# 3. تشغيل الاختبار
python manage.py test tests.test_authentication

# 4. إذا نجح، تطبيق في المشروع الفعلي
# apps/authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    national_id = models.CharField(max_length=10, unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.username and self.national_id:
            self.username = self.national_id[-4:]  # آخر 4 أرقام
        if not self.password and self.national_id:
            self.set_password(self.national_id[:4])  # أول 4 أرقام
        super().save(*args, **kwargs)

# 5. بعد التأكد من النجاح، حذف ملف الاختبار
rm tests/test_authentication.py
```

#### الأسبوع 3-4: إدارة الموظفين
```python
# apps/employees/models.py
from django.db import models
from django.contrib.auth import get_user_model
from apps.companies.models import Company

User = get_user_model()

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Position(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    requirements = models.TextField(blank=True)

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'نشط'),
        ('suspended', 'مجمد'),
        ('terminated', 'منتهي الخدمة'),
    ]
    
    # ربط بنموذج المستخدم
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # البيانات الشخصية
    employee_id = models.CharField(max_length=20, unique=True)
    national_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50, default='سعودي')
    
    # معلومات الاتصال
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField()
    
    # البيانات الوظيفية
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    hire_date = models.DateField()
    contract_type = models.CharField(max_length=20, default='permanent')
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    # حالة الموظف
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    termination_date = models.DateField(null=True, blank=True)
    termination_reason = models.TextField(blank=True)
    
    # ملفات
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def years_of_service(self):
        from datetime import date
        return (date.today() - self.hire_date).days // 365
    
    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"
```

#### الأسبوع 5-6: التصميم والواجهات
```html
<!-- templates/employees/employee_list.html -->
{% extends 'base/base.html' %}
{% load static %}

{% block title %}قائمة الموظفين{% endblock %}

{% block extra_css %}
<link href="{% static 'css/employees.css' %}" rel="stylesheet">
{% endblock %}

{% block content %}
<div class="container-fluid">
    <!-- رأس الصفحة -->
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2><i class="fas fa-users"></i> قائمة الموظفين</h2>
        <a href="{% url 'employees:add' %}" class="btn btn-primary">
            <i class="fas fa-plus"></i> إضافة موظف جديد
        </a>
    </div>

    <!-- فلاتر البحث -->
    <div class="card mb-4">
        <div class="card-body">
            <form method="get" class="row g-3">
                <div class="col-md-3">
                    <label class="form-label">البحث</label>
                    <input type="text" class="form-control" name="search" 
                           value="{{ request.GET.search }}" placeholder="اسم أو رقم الموظف">
                </div>
                <div class="col-md-3">
                    <label class="form-label">القسم</label>
                    <select class="form-select" name="department">
                        <option value="">جميع الأقسام</option>
                        {% for dept in departments %}
                        <option value="{{ dept.id }}" 
                                {% if request.GET.department == dept.id|stringformat:"s" %}selected{% endif %}>
                            {{ dept.name }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
                <div class="col-md-3">
                    <label class="form-label">الحالة</label>
                    <select class="form-select" name="status">
                        <option value="">جميع الحالات</option>
                        <option value="active" {% if request.GET.status == 'active' %}selected{% endif %}>نشط</option>
                        <option value="suspended" {% if request.GET.status == 'suspended' %}selected{% endif %}>مجمد</option>
                        <option value="terminated" {% if request.GET.status == 'terminated' %}selected{% endif %}>منتهي الخدمة</option>
                    </select>
                </div>
                <div class="col-md-3 d-flex align-items-end">
                    <button type="submit" class="btn btn-outline-primary me-2">
                        <i class="fas fa-search"></i> بحث
                    </button>
                    <a href="{% url 'employees:list' %}" class="btn btn-outline-secondary">
                        <i class="fas fa-times"></i> مسح
                    </a>
                </div>
            </form>
        </div>
    </div>

    <!-- جدول الموظفين -->
    <div class="card">
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-hover" id="employeesTable">
                    <thead class="table-dark">
                        <tr>
                            <th>الصورة</th>
                            <th>رقم الموظف</th>
                            <th>الاسم</th>
                            <th>القسم</th>
                            <th>المنصب</th>
                            <th>تاريخ التوظيف</th>
                            <th>الحالة</th>
                            <th>الإجراءات</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for employee in employees %}
                        <tr>
                            <td>
                                {% if employee.profile_picture %}
                                    <img src="{{ employee.profile_picture.url }}" 
                                         class="rounded-circle" width="40" height="40">
                                {% else %}
                                    <div class="bg-secondary rounded-circle d-flex align-items-center justify-content-center" 
                                         style="width: 40px; height: 40px;">
                                        <i class="fas fa-user text-white"></i>
                                    </div>
                                {% endif %}
                            </td>
                            <td>{{ employee.employee_id }}</td>
                            <td>{{ employee.full_name }}</td>
                            <td>{{ employee.department.name|default:"-" }}</td>
                            <td>{{ employee.position.title|default:"-" }}</td>
                            <td>{{ employee.hire_date|date:"Y/m/d" }}</td>
                            <td>
                                {% if employee.status == 'active' %}
                                    <span class="badge bg-success">نشط</span>
                                {% elif employee.status == 'suspended' %}
                                    <span class="badge bg-warning">مجمد</span>
                                {% else %}
                                    <span class="badge bg-danger">منتهي الخدمة</span>
                                {% endif %}
                            </td>
                            <td>
                                <div class="btn-group btn-group-sm">
                                    <a href="{% url 'employees:detail' employee.pk %}" 
                                       class="btn btn-outline-info" title="عرض">
                                        <i class="fas fa-eye"></i>
                                    </a>
                                    <a href="{% url 'employees:edit' employee.pk %}" 
                                       class="btn btn-outline-warning" title="تعديل">
                                        <i class="fas fa-edit"></i>
                                    </a>
                                    <button type="button" class="btn btn-outline-danger" 
                                            onclick="confirmDelete({{ employee.pk }})" title="حذف">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="8" class="text-center text-muted py-4">
                                <i class="fas fa-users fa-2x mb-2"></i><br>
                                لا توجد موظفين مطابقين للبحث
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>

            <!-- الترقيم -->
            {% if is_paginated %}
            <nav aria-label="ترقيم الصفحات">
                <ul class="pagination justify-content-center">
                    {% if page_obj.has_previous %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ page_obj.previous_page_number }}">السابق</a>
                        </li>
                    {% endif %}
                    
                    {% for num in page_obj.paginator.page_range %}
                        {% if page_obj.number == num %}
                            <li class="page-item active">
                                <span class="page-link">{{ num }}</span>
                            </li>
                        {% else %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                            </li>
                        {% endif %}
                    {% endfor %}
                    
                    {% if page_obj.has_next %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ page_obj.next_page_number }}">التالي</a>
                        </li>
                    {% endif %}
                </ul>
            </nav>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/employees.js' %}"></script>
<script>
function confirmDelete(employeeId) {
    if (confirm('هل أنت متأكد من حذف هذا الموظف؟')) {
        // إرسال طلب حذف عبر AJAX أو إعادة توجيه
        window.location.href = `/employees/delete/${employeeId}/`;
    }
}

// تفعيل DataTables للجدول
$(document).ready(function() {
    $('#employeesTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/ar.json'
        },
        pageLength: 25,
        responsive: true
    });
});
</script>
{% endblock %}
```

### المرحلة 2: الوظائف المتقدمة (6-8 أسابيع)

#### الأسبوع 7-8: نظام الحضور والانصراف
```python
# apps/attendance/models.py
from django.db import models
from django.utils import timezone
from apps.employees.models import Employee

class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('present', 'حاضر'),
        ('absent', 'غائب'),
        ('late', 'متأخر'),
        ('early_leave', 'انصراف مبكر'),
        ('overtime', 'عمل إضافي'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    
    # أوقات الحضور والانصراف
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    break_start_time = models.TimeField(null=True, blank=True)
    break_end_time = models.TimeField(null=True, blank=True)
    
    # الموقع الجغرافي
    check_in_location_lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    check_in_location_lng = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    check_out_location_lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    check_out_location_lng = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    
    # الحسابات
    work_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    overtime_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    late_minutes = models.IntegerField(default=0)
    early_leave_minutes = models.IntegerField(default=0)
    
    # الحالة والملاحظات
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['employee', 'date']
        ordering = ['-date', '-created_at']
    
    def calculate_work_hours(self):
        """حساب ساعات العمل"""
        if self.check_in_time and self.check_out_time:
            from datetime import datetime, timedelta
            
            # تحويل الأوقات لـ datetime للحساب
            check_in = datetime.combine(self.date, self.check_in_time)
            check_out = datetime.combine(self.date, self.check_out_time)
            
            # إذا كان وقت الخروج في اليوم التالي
            if check_out < check_in:
                check_out += timedelta(days=1)
            
            # حساب إجمالي الوقت
            total_time = check_out - check_in
            
            # خصم وقت الاستراحة إذا وجد
            if self.break_start_time and self.break_end_time:
                break_start = datetime.combine(self.date, self.break_start_time)
                break_end = datetime.combine(self.date, self.break_end_time)
                break_duration = break_end - break_start
                total_time -= break_duration
            
            # تحويل لساعات
            hours = total_time.total_seconds() / 3600
            
            # تحديد ساعات العمل العادية والإضافية
            standard_hours = 8  # ساعات العمل المعتادة
            
            if hours > standard_hours:
                self.work_hours = standard_hours
                self.overtime_hours = hours - standard_hours
            else:
                self.work_hours = hours
                self.overtime_hours = 0
            
            self.save()
    
    def calculate_late_minutes(self):
        """حساب دقائق التأخير"""
        if self.check_in_time:
            from datetime import time
            
            # وقت بداية العمل المحدد (يمكن جعله متغير حسب الموظف)
            work_start_time = time(8, 0)  # 8:00 صباحاً
            
            if self.check_in_time > work_start_time:
                from datetime import datetime, timedelta
                
                work_start = datetime.combine(self.date, work_start_time)
                actual_check_in = datetime.combine(self.date, self.check_in_time)
                
                late_duration = actual_check_in - work_start
                self.late_minutes = int(late_duration.total_seconds() / 60)
                
                if self.late_minutes > 0:
                    self.status = 'late'
            
            self.save()

# apps/attendance/api_views.py (للتطبيق المحمول)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import AttendanceRecord
from .utils import calculate_distance

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_in(request):
    """تسجيل الحضور عبر API"""
    try:
        employee = request.user.employee
        today = timezone.now().date()
        
        # التحقق من عدم وجود تسجيل حضور سابق لليوم
        attendance, created = AttendanceRecord.objects.get_or_create(
            employee=employee,
            date=today,
            defaults={'check_in_time': timezone.now().time()}
        )
        
        if not created and attendance.check_in_time:
            return Response({
                'error': 'تم تسجيل الحضور مسبقاً لهذا اليوم'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # الحصول على الموقع الجغرافي
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        
        if not latitude or not longitude:
            return Response({
                'error': 'يجب تفعيل الموقع الجغرافي'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # التحقق من الموقع (إذا كان ضمن النطاق المسموح)
        company_lat = employee.company.latitude  # يجب إضافة هذا للشركة
        company_lng = employee.company.longitude
        allowed_radius = employee.company.allowed_radius or 100  # متر
        
        distance = calculate_distance(
            float(latitude), float(longitude),
            float(company_lat), float(company_lng)
        )
        
        if distance > allowed_radius:
            return Response({
                'error': f'أنت خارج نطاق العمل المسموح ({distance:.0f} متر)',
                'warning': True,
                'distance': distance
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # تسجيل الحضور
        attendance.check_in_time = timezone.now().time()
        attendance.check_in_location_lat = latitude
        attendance.check_in_location_lng = longitude
        attendance.save()
        
        # حساب التأخير
        attendance.calculate_late_minutes()
        
        return Response({
            'message': 'تم تسجيل الحضور بنجاح',
            'time': attendance.check_in_time.strftime('%H:%M'),
            'late_minutes': attendance.late_minutes,
            'status': attendance.status
        })
        
    except Exception as e:
        return Response({
            'error': f'خطأ في تسجيل الحضور: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_out(request):
    """تسجيل الانصراف عبر API"""
    try:
        employee = request.user.employee
        today = timezone.now().date()
        
        # البحث عن سجل الحضور لليوم
        try:
            attendance = AttendanceRecord.objects.get(
                employee=employee,
                date=today
            )
        except AttendanceRecord.DoesNotExist:
            return Response({
                'error': 'لم يتم تسجيل الحضور لهذا اليوم'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if attendance.check_out_time:
            return Response({
                'error': 'تم تسجيل الانصراف مسبقاً لهذا اليوم'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # الحصول على الموقع الجغرافي
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        
        # تسجيل الانصراف
        attendance.check_out_time = timezone.now().time()
        attendance.check_out_location_lat = latitude
        attendance.check_out_location_lng = longitude
        attendance.save()
        
        # حساب ساعات العمل
        attendance.calculate_work_hours()
        
        return Response({
            'message': 'تم تسجيل الانصراف بنجاح',
            'time': attendance.check_out_time.strftime('%H:%M'),
            'work_hours': float(attendance.work_hours),
            'overtime_hours': float(attendance.overtime_hours)
        })
        
    except Exception as e:
        return Response({
            'error': f'خطأ في تسجيل الانصراف: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# apps/attendance/utils.py
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    حساب المسافة بين نقطتين جغرافيتين بالمتر
    باستخدام صيغة Haversine
    """
    # تحويل من درجات إلى راديان
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # صيغة Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # نصف قطر الأرض بالمتر
    r = 6371000
    
    # المسافة بالمتر
    return c * r
```

---

## 🛠 أدوات التطوير المساعدة

### 1. نظام تحليل الأخطاء
```python
# apps/system/error_analyzer.py
import logging
import traceback
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required

# إعداد نظام التسجيل
logger = logging.getLogger('hr_system')

class ErrorAnalyzer:
    """محلل الأخطاء الذكي"""
    
    @staticmethod
    def analyze_error(error_type, error_message, traceback_info):
        """تحليل الخطأ واقتراح حلول"""
        
        common_errors = {
            'DoesNotExist': {
                'description': 'الكائن المطلوب غير موجود في قاعدة البيانات',
                'solutions': [
                    'تحقق من صحة المعرف المرسل',
                    'تأكد من وجود البيانات في قاعدة البيانات',
                    'استخدم get_object_or_404 بدلاً من get'
                ]
            },
            'IntegrityError': {
                'description': 'خطأ في تكامل البيانات',
                'solutions': [
                    'تحقق من القيود الفريدة (unique constraints)',
                    'تأكد من وجود البيانات المطلوبة',
                    'راجع العلاقات بين الجداول'
                ]
            },
            'ValidationError': {
                'description': 'خطأ في التحقق من صحة البيانات',
                'solutions': [
                    'راجع قواعد التحقق في النماذج',
                    'تأكد من صحة تنسيق البيانات المدخلة',
                    'تحقق من القيود على الحقول'
                ]
            },
            'PermissionDenied': {
                'description': 'عدم وجود صلاحية للوصول',
                'solutions': [
                    'تحقق من صلاحيات المستخدم',
                    'راجع إعدادات الحماية',
                    'تأكد من تسجيل الدخول'
                ]
            }
        }
        
        # البحث عن النوع في الأخطاء الشائعة
        for error_key, error_info in common_errors.items():
            if error_key in error_type:
                return {
                    'type': error_type,
                    'message': error_message,
                    'description': error_info['description'],
                    'solutions': error_info['solutions'],
                    'severity': 'medium'
                }
        
        # خطأ غير معروف
        return {
            'type': error_type,
            'message': error_message,
            'description': 'خطأ غير محدد في النظام',
            'solutions': [
                'راجع ملف سجل الأخطاء للتفاصيل',
                'تحقق من إعدادات النظام',
                'اتصل بالدعم التقني'
            ],
            'severity': 'high'
        }

@require_POST
@staff_member_required
def analyze_system_errors(request):
    """API لتحليل أخطاء النظام"""
    try:
        # قراءة آخر الأخطاء من ملف السجل
        with open('logs/django.log', 'r', encoding='utf-8') as f:
            recent_logs = f.readlines()[-100:]  # آخر 100 سطر
        
        errors = []
        analyzer = ErrorAnalyzer()
        
        for line in recent_logs:
            if 'ERROR' in line:
                # استخراج معلومات الخطأ
                # (هذا مثال مبسط، يمكن تحسينه)
                parts = line.split(' - ')
                if len(parts) >= 2:
                    error_info = analyzer.analyze_error(
                        error_type='Unknown',
                        error_message=parts[-1].strip(),
                        traceback_info=''
                    )
                    errors.append(error_info)
        
        return JsonResponse({
            'success': True,
            'errors_count': len(errors),
            'errors': errors[:10],  # آخر 10 أخطاء
            'recommendations': [
                'قم بنسخ احتياطي دوري للبيانات',
                'راقب استخدام الذاكرة والمعالج',
                'حدث المكتبات للإصدارات الأحدث'
            ]
        })
        
    except Exception as e:
        logger.error(f"خطأ في تحليل الأخطاء: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'فشل في تحليل أخطاء النظام'
        })

# إضافة زر تحليل الأخطاء في القالب
```

```html
<!-- templates/base/base.html - إضافة زر تحليل الأخطاء -->
{% if user.is_staff %}
<div class="position-fixed bottom-0 end-0 p-3">
    <button type="button" class="btn btn-warning btn-sm" 
            onclick="analyzeSystemErrors()" id="errorAnalyzerBtn">
        <i class="fas fa-bug"></i> تحليل الأخطاء
    </button>
</div>

<script>
function analyzeSystemErrors() {
    const btn = document.getElementById('errorAnalyzerBtn');
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التحليل...';
    btn.disabled = true;
    
    fetch('/system/analyze-errors/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showErrorAnalysisModal(data);
        } else {
            alert('فشل في تحليل الأخطاء: ' + data.error);
        }
    })
    .catch(error => {
        alert('خطأ في الاتصال: ' + error.message);
    })
    .finally(() => {
        btn.innerHTML = '<i class="fas fa-bug"></i> تحليل الأخطاء';
        btn.disabled = false;
    });
}

function showErrorAnalysisModal(data) {
    // إنشاء مودال لعرض نتائج التحليل
    const modalHtml = `
        <div class="modal fade" id="errorAnalysisModal" tabindex="-1">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">
                            <i class="fas fa-bug"></i> تحليل أخطاء النظام
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <div class="alert alert-info">
                            <strong>عدد الأخطاء المكتشفة:</strong> ${data.errors_count}
                        </div>
                        
                        ${data.errors.map(error => `
                            <div class="card mb-3">
                                <div class="card-header">
                                    <strong>${error.type}</strong>
                                    <span class="badge bg-${error.severity === 'high' ? 'danger' : 'warning'} float-end">
                                        ${error.severity}
                                    </span>
                                </div>
                                <div class="card-body">
                                    <p><strong>الوصف:</strong> ${error.description}</p>
                                    <p><strong>الرسالة:</strong> ${error.message}</p>
                                    <strong>الحلول المقترحة:</strong>
                                    <ul>
                                        ${error.solutions.map(solution => `<li>${solution}</li>`).join('')}
                                    </ul>
                                </div>
                            </div>
                        `).join('')}
                        
                        <div class="mt-4">
                            <h6>التوصيات العامة:</h6>
                            <ul>
                                ${data.recommendations.map(rec => `<li>${rec}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">إغلاق</button>
                        <button type="button" class="btn btn-primary" onclick="downloadErrorReport()">
                            <i class="fas fa-download"></i> تحميل التقرير
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // إزالة المودال القديم إن وجد
    const existingModal = document.getElementById('errorAnalysisModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    // إضافة المودال الجديد
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    
    // عرض المودال
    const modal = new bootstrap.Modal(document.getElementById('errorAnalysisModal'));
    modal.show();
}
</script>
{% endif %}
```

---

## 📋 دليل التشغيل اليومي

### الروتين اليومي للمطور:

#### 1. بداية اليوم (الصباح):
```bash
# تفعيل البيئة الافتراضية
source venv/bin/activate  # أو venv\Scripts\activate في Windows

# تحديث المشروع من Git (إذا كان مشترك)
git pull origin main

# تشغيل migrations جديدة إن وجدت
python manage.py migrate

# تشغيل الخادم
python manage.py runserver
```

#### 2. أثناء التطوير:
```bash
# إنشاء ملف اختبار للميزة الجديدة
touch tests/test_new_feature.py

# كتابة الاختبار وتشغيله
python manage.py test tests.test_new_feature

# بعد النجاح، تطبيق في المشروع الفعلي
# ... كتابة الكود ...

# اختبار شامل
python manage.py test

# إنشاء migrations إذا تغيرت النماذج
python manage.py makemigrations

# حذف ملف الاختبار بعد النجاح
rm tests/test_new_feature.py
```

#### 3. نهاية اليوم:
```bash
# جمع الملفات الثابتة
python manage.py collectstatic --noinput

# نسخ احتياطي من قاعدة البيانات
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# حفظ التغييرات في Git
git add .
git commit -m "وصف التغييرات اليوم"
git push origin main
```

---

## 🔍 مراجعة الكود (Code Review)

### معايير مراجعة الكود:

#### 1. التحقق من الجودة:
- هل الكود نظيف وقابل للقراءة؟
- هل تتبع مبادئ PEP 8؟
- هل الدوال والمتغيرات لها أسماء واضحة؟
- هل هناك تعليقات توضيحية كافية؟

#### 2. التحقق من الأمان:
- هل تم التحقق من المدخلات؟
- هل تم استخدام CSRF protection؟
- هل كلمات المرور مشفرة؟
- هل تم تطبيق صلاحيات الوصول؟

#### 3. التحقق من الأداء:
- هل الاستعلامات محسنة؟
- هل تم تجنب N+1 queries؟
- هل الملفات الثابتة مضغوطة؟
- هل تم استخدام caching مناسب؟

---

## 📝 نصائح مهمة للتطوير

### 1. إدارة البيانات الوهمية:
```python
# إنشاء بيانات وهمية للاختبار
# management/commands/create_sample_data.py
from django.core.management.base import BaseCommand
from apps.companies.models import Company
from apps.employees.models import Employee, Department
from faker import Faker
import random

class Command(BaseCommand):
    help = 'إنشاء بيانات وهمية للاختبار'
    
    def handle(self, *args, **options):
        fake = Faker('ar_SA')  # بيانات عربية
        
        # إنشاء شركة وهمية
        company = Company.objects.create(
            name=fake.company(),
            commercial_registration=fake.numerify('##########'),
            tax_number=fake.numerify('###########'),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email()
        )
        
        # إنشاء أقسام وهمية
        departments = []
        for _ in range(5):
            dept = Department.objects.create(
                company=company,
                name=fake.job(),
                description=fake.text()
            )
            departments.append(dept)
        
        # إنشاء موظفين وهميين
        for i in range(50):
            employee = Employee.objects.create(
                employee_id=f'EMP{i+1:04d}',
                national_id=fake.numerify('##########'),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=22, maximum_age=60),
                gender=random.choice(['M', 'F']),
                phone=fake.phone_number(),
                email=fake.email(),
                address=fake.address(),
                company=company,
                department=random.choice(departments),
                hire_date=fake.date_between(start_date='-5y', end_date='today'),
                basic_salary=random.randint(3000, 15000)
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'تم إنشاء {50} موظف وهمي بنجاح')
        )
```

### 2. نظام النسخ الاحتياطي التلقائي:
```python
# scripts/auto_backup.py
import os
import datetime
from django.core.management import execute_from_command_line

def create_backup():
    """إنشاء نسخة احتياطية تلقائية"""
    today = datetime.date.today().strftime('%Y%m%d')
    backup_file = f'backups/backup_{today}.json'
    
    # إنشاء مجلد النسخ الاحتياطي إذا لم يكن موجود
    os.makedirs('backups', exist_ok=True)
    
    # إنشاء النسخة الاحتياطية
    execute_from_command_line(['manage.py', 'dumpdata', '--output', backup_file])
    
    print(f'تم إنشاء نسخة احتياطية: {backup_file}')

if __name__ == '__main__':
    create_backup()
```

---

**🚀 جاهز للبدء في التطوير!**

**الخطوة التالية**: ابدأ بتطبيق نظام المصادقة والشركات كما هو موضح في المرحلة الأولى.
