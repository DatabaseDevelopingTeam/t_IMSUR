from django.db import models

# Create your models here.


class 定期任务(models.Model):
    巡查日期=models.DateField('巡查日期')
    #道路编号=models.ForeignKey(道路基本档案,verbose_name='巡查道路编号',related_name='roadNumber',on_delete=models.CASCADE)
    #道路名称=models.ForeignKey(道路基本档案,verbose_name='巡查道路名称',on_delete=models.CASCADE,related_name='roadName')
    #道路等级=models.ForeignKey(道路基本档案,verbose_name='巡查道路等级',on_delete=models.CASCADE,related_name='roadLevel')

    class Meta:
        verbose_name = '定期任务'
        verbose_name_plural = '定期任务'
