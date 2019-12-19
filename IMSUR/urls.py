"""
城镇道路养护信息管理系统
Information management system of urban road maintenance
"""

from django.contrib import admin
from django.urls import path, include
from login import views as loginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews.login),
    path('municipalManagement/',include('municipalManagementUI.urls')),
    path('patrolManagement/',include('patrolManagementUI.urls')),
]
