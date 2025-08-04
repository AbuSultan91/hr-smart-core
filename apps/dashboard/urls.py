"""
HR Smart Core - Dashboard URLs
روابط لوحة التحكم
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
]