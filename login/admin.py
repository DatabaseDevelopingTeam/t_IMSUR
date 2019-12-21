from django.contrib import admin

from django.contrib import admin
from .models import 职工


class EmployeeAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ['工号', '姓名', '性别', '职能']
    # 可以点击的字段
    list_display_links = ['姓名']
    # list_filter = ['ticket','密码']
    # 可以搜索的字段
    search_fields = ['姓名']
    # 可以在全表中直接修改的字段
    # list_editable = ['姓名', '性别', '职能']
    # 排除字段
    exclude = ['ticket']


admin.site.register(职工, EmployeeAdmin)
