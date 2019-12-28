"""
城镇道路养护信息管理系统
Information management system of urban road maintenance
"""
from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from login import views as loginViews
from . import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews.forwardToLogin),  # 重定向到登录页面
    path('login/', loginViews.login),  # 登录验证
    path('ajaxEmployeeIdCheck/', loginViews.ajaxEmployeeIdCheck),  # 静态检测工号是否存在
    # path('ajaxPwdCheck/', loginViews.ajaxPwdCheck),  # 静态检测工号是否存在
    path('trueLogin/', loginViews.trueLogin),  # 提交表单登录
    path('municipalManagement/', include('municipalManagementUI.urls')),
    path('patrolManagement/', include('patrolManagementUI.urls')),
]

handler404 = views.page_not_found
handler500 = views.page_error
