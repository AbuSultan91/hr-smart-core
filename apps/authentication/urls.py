"""
HR Smart Core - Authentication URLs
روابط نظام المصادقة
"""

from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('check-username/', views.check_username, name='check_username'),
]