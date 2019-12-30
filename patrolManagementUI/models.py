from django.db import models
from municipalManagementUI import models as model_municipalManagementUI


# Create your models here.


class 定期巡查(models.Model):
    巡查日期 = models.DateField('巡查日期')
    巡查道路 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, null=True)
    巡查状态 = models.CharField('巡查状态', max_length=20, choices=(('1', '未巡查'), ('2', '已巡查')), default='未巡查')

    class Meta:
        verbose_name = '定期巡查'
        verbose_name_plural = '定期巡查'


class 定期检测记录(models.Model):
    定期检查记录编号 = models.AutoField('定期检查记录编号', primary_key=True)
    巡查人员 = models.ForeignKey(model_municipalManagementUI.职工, related_name='定期巡查引用职工', on_delete=models.CASCADE,
                             verbose_name='巡查人员', null=True)
    道路编号 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, verbose_name='道路编号',
                             default='1')
    # 平整度检测记录编号=models.OneToOneField(路面平整度检测记录,on_delete=models.CASCADE)
    巡查日期 = models.DateField('巡查日期', null=False, auto_now_add=True)

    class Meta:
        verbose_name='定期检测记录'
        verbose_name_plural='定期检测记录'


class 路面平整度检测记录(models.Model):
    平整度检测记录编号 = models.AutoField('平整度检测记录编号', primary_key=True)
    定期检查记录编号 = models.OneToOneField(定期检测记录, on_delete=models.CASCADE, verbose_name='定期检查记录编号', default='1')
    IRI = models.FloatField('平整度指数',null=False)
    备注 = models.CharField(max_length=100)

    class Meta:
        verbose_name = '路面平整度检测记录'
        verbose_name_plural = '路面平整度检测记录'


class 路面定期检查损害记录(models.Model):
    定期巡察损害记录编号 = models.AutoField('定期巡察损害记录编号', primary_key=True)
    定期检查记录编号 = models.ForeignKey(定期检测记录, on_delete=models.CASCADE, verbose_name='定期检查记录编号', default='1')
    路面类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='路面类型',
                             related_name='定期巡查损害记录引用路面类型',default='1')
    损坏类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='损坏类型',
                             related_name='定期巡查损害记录引用损坏类型',default='1')
    起止位置 = models.CharField('起止位置', null=False, max_length=100)
    检查总长 = models.FloatField('检查总长', null=False)
    检查总宽 = models.FloatField('检查总宽', null=False)
    损坏长 = models.FloatField('损坏长', null=False)
    损坏宽 = models.FloatField('损坏宽', null=False)
    损坏高 = models.FloatField('损坏高', null=False)
    损坏位置及情况描述 = models.CharField('损坏位置及情况描述', max_length=100, null=False)

    class Meta:
        verbose_name = '路面定期检查损害记录'
        verbose_name_plural = '路面定期检查损害记录'


class 日常巡查(models.Model):
    巡查日期 = models.DateField('巡查日期')
    巡查道路 = models.ForeignKey(model_municipalManagementUI.道路基本档案, related_name='no', on_delete=models.CASCADE, null=True)
    巡查状态 = models.CharField('巡查状态', max_length=20, choices=(('1', '未巡查'), ('2', '已巡查')), default='未巡查')

    class Meta:
        verbose_name = '日常巡查'
        verbose_name_plural = '日常巡查'


class 日常巡查记录(models.Model):
    日常巡查记录编号 = models.AutoField('日常巡查记录编号', primary_key=True)
    巡查人员 = models.ForeignKey(model_municipalManagementUI.职工, related_name='日常巡查引用职工', on_delete=models.CASCADE,
                             verbose_name='巡查人员', null=True)
    道路编号 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, verbose_name='道路编号',
                             default='1')
    巡查日期 = models.DateField('巡查日期', null=False)

    class Meta:
        verbose_name = '日常巡查记录'
        verbose_name_plural = '日常巡查记录'


class 日常巡查损害记录(models.Model):
    日常巡查损害记录编号 = models.AutoField('日常巡查损害记录编号', primary_key=True)
    日常巡查记录编号 = models.ForeignKey(日常巡查记录, on_delete=models.CASCADE, verbose_name='日常巡查记录编号', default='1')
    路面类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='路面类型',
                             related_name='日常巡查损坏记录引用路面类型',default='1')
    损坏类型 = models.ForeignKey(model_municipalManagementUI.路面损坏类型, on_delete=models.CASCADE, verbose_name='损坏类型',
                             related_name='日常巡查损坏记录引用损坏类型',default='1')
    损坏位置及情况描述 = models.CharField('损坏位置及情况描述', max_length=100)

    class Meta:
        verbose_name = '日常巡查损害记录'
        verbose_name_plural = '日常巡查损害记录'
