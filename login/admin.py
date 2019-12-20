from django.contrib import admin

from django.contrib import admin
from .models import 职工


@admin.register(职工)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('工号', '姓名', '性别', '职能')
    list_display_links = ('姓名', '性别', '职能')
