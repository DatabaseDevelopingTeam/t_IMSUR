from django.db import models


# Create your models here.


class 职工表(models.Model):
    工号 = models.CharField('工号', max_length=12, primary_key=True)
    姓名 = models.CharField('姓名', max_length=40, null=False)
    性别 = models.CharField('性别', max_length=2, null=False)
    职能 = models.CharField('职能', max_length=20)
    密码 = models.CharField('密码', max_length=40)

    class Meta:
        verbose_name = '职工表'
        verbose_name_plural = '职工表'
