"""
HR Smart Core - Main URLs
الروابط الرئيسية للنظام
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# تخصيص عنوان لوحة الإدارة
admin.site.site_header = 'HR Smart Core - إدارة النظام'
admin.site.site_title = 'HR Smart Core'
admin.site.index_title = 'لوحة تحكم المدير'

def redirect_to_dashboard(request):
    """توجيه الصفحة الرئيسية إلى لوحة التحكم"""
    return redirect('dashboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('', redirect_to_dashboard),  # توجيه الصفحة الرئيسية
]

# إضافة ملفات الوسائط في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else '')
