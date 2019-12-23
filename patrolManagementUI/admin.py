from django.contrib import admin
from .models import 定期任务

# Register your models here.


@admin.register(定期任务)
class RegularTaskAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = [id, '巡查日期', '道路编号', '道路名称']
    # 可以点击的字段
    list_display_links = ['巡查日期']
    list_filter = ['巡查日期','道路等级']
    # 可以搜索的字段
    search_fields = ['巡查日期', '道路编号','道路名称']
    # 可以在全表中直接修改的字段
    # list_editable = ['姓名', '性别', '职能']
    # 排除字段
    # 只可读字段
    # readonly_fields = ['工号', '密码']
    # list_editable = ['姓名','性别']
