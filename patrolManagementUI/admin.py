from django.contrib import admin
from .models import 定期巡查
from .models import 日常巡查

# Register your models here.


@admin.register(定期巡查)
class RegularTaskAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = [id, '巡查日期']
    # 可以点击的字段
    list_display_links = ['巡查日期']
    list_filter = ['巡查日期']
    # 可以搜索的字段
    search_fields = ['巡查日期']


@admin.register(日常巡查)
class DailyTaskAdmin(admin.ModelAdmin):
    #要展示的字段
    list_display=[id,'巡查日期']
    #可以点击的字段
    list_display_links=['巡查日期']
    list_filter=['巡查日期']
    #可以搜索的字段
    search_fields=['巡查日期']
