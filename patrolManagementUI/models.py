from django.db import models
from municipalManagementUI import models as model_municipalManagementUI


# Create your models here.


class 定期巡查任务(models.Model):
    巡查日期 = models.DateField('巡查日期')
    巡查道路 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, null=True)
    巡查状态 = models.CharField('巡查状态', max_length=20, choices=(('1', '未巡查'), ('2', '已巡查')), default='未巡查')

    class Meta:
        verbose_name = '定期巡查任务'
        verbose_name_plural = '定期巡查任务'

    def roadId(self):
        return self.巡查道路.道路编号

    def roadName(self):
        return self.巡查道路.道路名称

    roadId.short_description = '道路编号'
    roadName.short_description = '道路名称'


class 定期检测记录(models.Model):
    定期检查记录编号 = models.AutoField('编号', primary_key=True)
    巡查人员 = models.ForeignKey(model_municipalManagementUI.职工, related_name='定期巡查引用职工', on_delete=models.CASCADE,
                             verbose_name='巡查人员', null=True)
    道路编号 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, verbose_name='道路编号',
                             default='1')
    巡查日期 = models.DateField('巡查日期', null=False, auto_now_add=True)

    class Meta:
        verbose_name='定期检测记录'
        verbose_name_plural='定期检测记录'

    def __str__(self):
        return str(self.定期检查记录编号)

    def roadName(self):
        return self.道路编号.道路名称

    roadName.short_description = '道路名称'

    def yearOfDate(self):
        return self.巡查日期.year


class 路面平整度检测记录(models.Model):
    平整度检测记录编号 = models.AutoField('编号', primary_key=True)
    定期检查记录编号 = models.OneToOneField(定期检测记录, on_delete=models.CASCADE, verbose_name='定期检查记录编号', default='1')
    IRI = models.FloatField('平整度指数',null=False)
    备注 = models.TextField(max_length=100,verbose_name='备注')

    class Meta:
        verbose_name = '路面平整度检测记录'
        verbose_name_plural = '路面平整度检测记录'


class 路面定期检查损害记录(models.Model):
    定期巡察损害记录编号 = models.AutoField('编号', primary_key=True)
    定期检查记录编号 = models.ForeignKey(定期检测记录, on_delete=models.CASCADE, verbose_name='定期检查记录编号', default='1')
    损坏类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='损坏类型',
                             related_name='定期巡查损害记录引用损坏类型',default='1')
    起止位置 = models.CharField('起止位置', null=False, max_length=100)
    检查总长 = models.FloatField('检查总长', null=False,default=0)
    检查总宽 = models.FloatField('检查总宽', null=False,default=0)
    损坏长 = models.FloatField('损坏长', null=False,default=1)
    损坏宽 = models.FloatField('损坏宽', null=False,  default=1)
    损坏高 = models.FloatField('损坏高', null=False,default=1)
    损坏位置及情况描述 = models.TextField('损坏位置及情况描述', max_length=100, null=True)
    备注=models.TextField('备注',max_length=100,null=True)

    class Meta:
        verbose_name = '路面定期检查损害记录'
        verbose_name_plural = '路面定期检查损害记录'


class 日常巡查任务(models.Model):
    巡查日期 = models.DateField('巡查日期')
    巡查道路 = models.ForeignKey(model_municipalManagementUI.道路基本档案, related_name='no', on_delete=models.CASCADE, null=True)
    巡查状态 = models.CharField('巡查状态', max_length=20, choices=(('1', '未巡查'), ('2', '已巡查')), default='1')

    class Meta:
        verbose_name = '日常巡查任务'
        verbose_name_plural = '日常巡查任务'

    def roadId(self):
        return self.巡查道路.道路编号

    def roadName(self):
        return self.巡查道路.道路名称

    roadId.short_description = '道路编号'
    roadName.short_description = '道路名称'


class 日常巡查记录(models.Model):
    日常巡查记录编号 = models.AutoField('编号', primary_key=True)
    巡查人员 = models.ForeignKey(model_municipalManagementUI.职工, related_name='日常巡查引用职工', on_delete=models.CASCADE,
                             verbose_name='巡查人员', null=True)
    道路编号 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, verbose_name='道路编号',
                             default='1')
    巡查日期 = models.DateField('巡查日期', null=False)

    class Meta:
        verbose_name = '日常巡查记录'
        verbose_name_plural = '日常巡查记录'

    def __str__(self):
        return str(self.日常巡查记录编号)+'  '+str(self.巡查日期)

    def roadName(self):
        return self.道路编号.道路名称

    roadName.short_description = '道路名称'


class 日常巡查损害记录(models.Model):
    日常巡查损害记录编号 = models.AutoField('编号', primary_key=True)
    日常巡查记录编号 = models.ForeignKey(日常巡查记录, on_delete=models.CASCADE, verbose_name='日常巡查记录编号', default='1')
    # 路面类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='路面类型',
    #                         related_name='日常巡查损坏记录引用路面类型',default='1')
    损坏类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='损坏类型',
                             related_name='日常巡查损坏记录引用损坏类型',default='1')
    损坏位置及情况描述 = models.TextField('损坏位置及情况描述', max_length=100)
    备注=models.TextField('备注',max_length=100)

    class Meta:
        verbose_name = '日常巡查损害记录'
        verbose_name_plural = '日常巡查损害记录'

    def roadType(self):
        return self.损坏类型.要引用的路面类型

    roadType.short_description = '路面类型'