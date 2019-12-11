"""
城镇道路养护信息管理系统
Information management system of urban road maintenance
"""

from django.contrib import admin
from django.urls import path
from HelloWorld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.index),
]
