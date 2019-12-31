from django.contrib import admin
from .models import 定期巡查任务
from .models import 日常巡查任务
from .models import 定期检测记录
from .models import 路面平整度检测记录
from .models import 路面定期检查损害记录
from .models import 日常巡查记录
from .models import 日常巡查损害记录


# Register your models here.


@admin.register(定期巡查任务)
class RegularTaskAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ['巡查日期', 'roadId','roadName','巡查状态']
    # 可以点击的字段
    # list_display_links = []
    list_filter = ['巡查日期', '巡查状态']
    # 可以搜索的字段
    search_fields = ['巡查日期', 'roadId','roadName']


@admin.register(日常巡查任务)
class DailyTaskAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ['巡查日期', 'roadId','roadName', '巡查状态']
    # 可以点击的字段
    # list_display_links = []
    list_filter = ['巡查日期', '巡查状态']
    # 可以搜索的字段
    search_fields = ['巡查日期', 'roadId','roadName']


@admin.register(定期检测记录)
class DQJCJL(admin.ModelAdmin):
    list_display = ['定期检查记录编号','巡查人员', '道路编号','roadName','巡查日期']
    list_filter = ['巡查日期','巡查人员']
    search_fields = ['定期检查记录编号', '道路编号', '巡查日期','roadName']
    # 按照什么进行排序
    # ordering = ['巡查日期']


@admin.register(路面平整度检测记录)
class LMPZDJCJL(admin.ModelAdmin):
    list_display = ['平整度检测记录编号', '定期检查记录编号', 'IRI']
    # list_display_links = ['备注']
    search_fields = ['平整度检测记录编号', '定期检查记录编号', 'IRI']


@admin.register(路面定期检查损害记录)
class LMDQJCSHJL(admin.ModelAdmin):
    list_display = ['定期巡察损害记录编号', '定期检查记录编号', '路面类型', '损坏类型']
    list_filter = ['路面类型','损坏类型','定期检查记录编号']
    # list_display_links = ['定期巡察损害记录编号']
    search_fields = ['定期巡察损害记录编号', '定期检查记录编号', '路面类型', '损坏类型']


@admin.register(日常巡查记录)
class RCXXJL(admin.ModelAdmin):
    list_display = ['日常巡查记录编号', '道路编号','roadName', '巡查人员', '巡查日期']
    list_filter = ['巡查人员','巡查日期']
    search_fields = ['日常巡查记录编号', '道路编号', '巡查人员', '巡查日期']


@admin.register(日常巡查损害记录)
class RCXCSHJL(admin.ModelAdmin):
    list_display = ['日常巡查损害记录编号','日常巡查记录编号','roadType','损坏类型','损坏位置及情况描述']
    # list_display_links = ['日常巡查损害记录编号']
    list_filter = ['损坏类型']
    search_fields = ['日常巡查损害记录编号','日常巡查记录编号','roadType','损坏类型']
