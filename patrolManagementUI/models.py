from django.db import models
from municipalManagementUI import models as model_municipalManagementUI

# Create your models here.


class 定期任务(models.Model):
    巡查日期=models.DateField('巡查日期')
    道路基本档案=models.ForeignKey(model_municipalManagementUI.道路基本档案,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '定期任务'
        verbose_name_plural = '定期任务'
