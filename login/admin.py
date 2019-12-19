from django.contrib import admin

from django.contrib import admin
from .models import 职工表


@admin.register(职工表)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('姓名', '性别', '职能', '密码')
