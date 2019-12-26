from django.db import models
from municipalManagementUI import models as model_municipalManagementUI


# Create your models here.


class 定期巡查(models.Model):
    巡查日期 = models.DateField('巡查日期')
    道路基本档案 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '定期巡查'
        verbose_name_plural = '定期巡查'


class 日常巡查(models.Model):
    巡查日期 = models.DateField('巡查日期')
    道路编号 = models.ForeignKey(model_municipalManagementUI.道路基本档案,related_name='no',on_delete=models.CASCADE,null=True)
    道路名称=models.ForeignKey(model_municipalManagementUI.道路基本档案,related_name='name',on_delete=models.CASCADE,null=True)
    #道路基本档案 = models.ForeignKey(model_municipalManagementUI.道路基本档案, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '日常巡查'
        verbose_name_plural = '日常巡查'
