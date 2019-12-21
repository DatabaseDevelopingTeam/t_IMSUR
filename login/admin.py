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
    # 只可读字段
    # readonly_fields = ['工号', '密码']
    # list_editable = ['姓名','性别']

    fieldsets = (
        ('基础信息',
         {
             'fields': ('姓名', '性别')
         }),
        ('高级选项',
         dict(classes='collapse', fields=('工号', '密码', '职能')))
    )


admin.site.register(职工, EmployeeAdmin)
