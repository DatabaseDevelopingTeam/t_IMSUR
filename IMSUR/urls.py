"""
城镇道路养护信息管理系统
Information management system of urban road maintenance
"""

from django.contrib import admin
from django.urls import path, include
from login import views as loginViews
from django.views.generic.base import RedirectView

from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews.forwardToLogin),  # 重定向到登录页面
    path('login/', loginViews.login),  # 登录验证
    path('logout/', loginViews.logout),  # 登出
    path('ajaxEmployeeIdCheck/', loginViews.ajaxEmployeeIdCheck),  # 静态检测工号是否存在
    # path('ajaxPwdCheck/', loginViews.ajaxPwdCheck),  # 静态检测工号是否存在
    path('trueLogin/', loginViews.trueLogin),  # 提交表单登录
    path('municipalManagement/', include('municipalManagementUI.urls')),  # 市政管理主页面
    path('patrolManagement/', include('patrolManagementUI.urls')),  # 巡查管理主页面
    path('favicon.ico/', RedirectView.as_view(url='/static/favicon.ico'))  # 网站图标
]

handler404 = loginViews.page_not_found
