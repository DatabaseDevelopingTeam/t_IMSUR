from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class 职工(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    工号 = models.CharField('工号', max_length=12, primary_key=True)
    姓名 = models.CharField('姓名', max_length=40, null=False)
    性别 = models.CharField('性别', max_length=2, choices=(('1', '男'), ('2', '女')), null=False, default='男')
    职能 = models.CharField('职能', max_length=20, choices=(('1', '市政道路管理'), ('2', '道路巡查养护')))
    密码 = models.CharField('密码', max_length=40)
    ticket = models.CharField('ticket', max_length=30, null=True,blank=True)  # 令牌

    class Meta:
        verbose_name = '职工'
        verbose_name_plural = '职工'
