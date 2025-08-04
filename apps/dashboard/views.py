"""
HR Smart Core - Dashboard Views
عرض لوحة التحكم الرئيسية
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count
from datetime import date, timedelta


@login_required
def dashboard_view(request):
    """لوحة التحكم الرئيسية"""
    
    # إحصائيات أساسية
    try:
        from apps.employees.models import Employee
        from apps.attendance.models import AttendanceRecord
        from apps.leaves.models import LeaveRequest
        from apps.payroll.models import Payroll
        
        # إجمالي الموظفين
        total_employees = Employee.objects.filter(is_active=True).count()
        
        # الحاضرون اليوم
        today = date.today()
        present_today = AttendanceRecord.objects.filter(
            date=today,
            status='present'
        ).count()
        
        # طلبات الإجازة المعلقة
        pending_leaves = LeaveRequest.objects.filter(
            status='pending'
        ).count()
        
        # كشوف الرواتب هذا الشهر
        current_month = today.month
        current_year = today.year
        payrolls_this_month = Payroll.objects.filter(
            month=current_month,
            year=current_year
        ).count()
        
    except Exception as e:
        # في حالة عدم وجود بيانات أو خطأ
        total_employees = 0
        present_today = 0
        pending_leaves = 0
        payrolls_this_month = 0
    
    context = {
        'current_date': timezone.now().date(),
        'total_employees': total_employees,
        'present_today': present_today,
        'pending_leaves': pending_leaves,
        'payrolls_this_month': payrolls_this_month,
    }
    
    return render(request, 'dashboard/dashboard.html', context)