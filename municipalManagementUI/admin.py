from django.contrib import admin
from . import models


@admin.register(models.道路等级)
class RoadLevelAdmin(admin.ModelAdmin):
    list_display = ['道路等级']
    list_display_links = ['道路等级']


@admin.register(models.路面类型)
class RoadTypeAdmin(admin.ModelAdmin):
    list_display_links = ['路面类型']
    list_display = ['路面类型']


@admin.register(models.路面损坏类型)
class RoadDamageTypeAdmin(admin.ModelAdmin):
    list_display_links = ['损坏类型']
    list_display = ['损坏类型']


@admin.register(models.车行道)
class RoadWayAdmin(admin.ModelAdmin):
    list_display_links = ['车行道编号']
    list_display = ['车行道编号']


@admin.register(models.道路基本档案)
class RoadBasicArchiveAdmin(admin.ModelAdmin):
    list_display_links = ['道路名称']
    list_display = ['道路名称','道路编号']


@admin.register(models.职工)
class EmployeeAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = [id, '工号', '姓名', '性别', '职能']
    # 可以点击的字段
    list_display_links = ['工号']
    list_filter = ['性别', '职能']
    # 可以搜索的字段
    search_fields = ['工号', '姓名']
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
