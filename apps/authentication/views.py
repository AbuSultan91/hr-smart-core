"""
HR Smart Core - Authentication Views
عرض المصادقة ونظام تسجيل الدخول
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def login_view(request):
    """عرض تسجيل الدخول"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'مرحباً بك {user.get_full_name() or user.username}')
                    
                    # التوجه إلى الصفحة المطلوبة أو لوحة التحكم
                    next_url = request.GET.get('next', 'dashboard')
                    return redirect(next_url)
                else:
                    messages.error(request, 'هذا الحساب معطل، يرجى التواصل مع الإدارة')
            else:
                messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
        else:
            messages.error(request, 'يرجى إدخال اسم المستخدم وكلمة المرور')
    
    return render(request, 'auth/login.html')


@login_required
def logout_view(request):
    """تسجيل الخروج"""
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('auth:login')


@login_required
def profile_view(request):
    """عرض الملف الشخصي"""
    return render(request, 'auth/profile.html', {
        'user': request.user
    })


@csrf_exempt
@require_http_methods(["POST"])
def check_username(request):
    """فحص توفر اسم المستخدم عبر AJAX"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        
        if not username:
            return JsonResponse({'available': False, 'message': 'اسم المستخدم مطلوب'})
        
        from django.contrib.auth.models import User
        exists = User.objects.filter(username=username).exists()
        
        return JsonResponse({
            'available': not exists,
            'message': 'اسم المستخدم متاح' if not exists else 'اسم المستخدم مستخدم بالفعل'
        })
    except:
        return JsonResponse({'available': False, 'message': 'خطأ في الخادم'})
