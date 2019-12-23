from django.contrib.auth.models import User
from django.db import models


class 道路等级(models.Model):
    道路等级 = models.CharField('道路等级', primary_key=True, max_length=4, choices=(
        ('1', '一级'), ('2', '二级'), ('3', '三级'), ('４', '四级')))

    class Meta:
        verbose_name_plural = '道路等级'
        verbose_name: str = '道路等级'


# Create your models here.
class 道路基本档案(models.Model):
    道路编号 = models.CharField('道路编号', primary_key=True, max_length=100)
    # 车行道=models.OneToOneField(车行道,on_delete=models.CASCADE)
    道路等级=models.ForeignKey(道路等级,on_delete=models.CASCADE, verbose_name='道路等级', default='1')
    道路名称 = models.CharField('道路名称', max_length=100, null=False)
    道路走向 = models.CharField('道路走向', max_length=100, null=False)
    起点 = models.CharField('起点', max_length=100, null=False)
    终点 = models.CharField('终点', max_length=100, null=False)
    设计单位 = models.CharField('设计单位', max_length=100, null=False)
    施工单位 = models.CharField('施工单位', max_length=100, null=False)
    路面等级 = models.CharField('路面等级', max_length=10, null=False)
    设计时速 = models.IntegerField('设计时速', null=False)
    路幅宽度范围 = models.CharField('路幅宽度范围', max_length=100, null=False)
    道路长度 = models.FloatField('道路长度', null=False)
    道路面积 = models.FloatField('道路面积', null=False)
    AADT = models.FloatField('AADT', null=False)
    交通量等级 = models.CharField('交通量等级', max_length=4, null=False)
    所属乡镇 = models.CharField('所属乡镇', max_length=100, null=False)
    管理分类 = models.CharField('管理分类', max_length=50, null=False)
    管理单位 = models.CharField('管理单位', max_length=50, null=False)
    养护单位 = models.CharField('养护单位', max_length=50, null=False)
    建造年月 = models.DateField('建造年月', null=False)


class 职工(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    工号 = models.CharField(verbose_name='工号', max_length=12, primary_key=True)
    姓名 = models.CharField(verbose_name='姓名', max_length=40, null=False)
    性别 = models.CharField(verbose_name='性别', max_length=2, choices=(('1', '男'), ('2', '女')), null=False, default='男')
    职能 = models.CharField(verbose_name='职能', max_length=20, choices=(('1', '市政道路管理'), ('2', '道路巡查养护')),
                          default='道路巡查养护')
    密码 = models.CharField(verbose_name='密码', max_length=40)
    ticket = models.CharField('ticket', max_length=30, null=True, blank=True)  # 令牌

    def __unicode__(self):
        return self.姓名

    class Meta:
        verbose_name = '职工'
        verbose_name_plural = '职工'
