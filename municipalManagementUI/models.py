from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class 路面类型(models.Model):
    路面类型 = models.CharField(verbose_name='路面类型', primary_key=True, max_length=12)

    class Meta:
        verbose_name_plural = '路面类型'
        verbose_name = '路面类型'

    def __unicode__(self):
        return self.路面类型

    def __str__(self):
        return self.路面类型


class 路面损坏类型(models.Model):
    要引用的路面类型 = models.ForeignKey(路面类型, on_delete=models.CASCADE, related_name='rn路面类型', verbose_name='路面类型')
    损坏类型 = models.CharField(verbose_name='损坏类型', max_length=40, primary_key=True)
    损坏面积计算方法代号 = models.PositiveSmallIntegerField(verbose_name='损坏面积计算方法代号', null=False, default=1)

    class Meta:
        verbose_name_plural = '路面损坏类型'
        verbose_name = '路面损坏类型'

    def __unicode__(self):
        return u'%s %s' % (self.要引用的路面类型.路面类型, self.损坏类型)

    def __str__(self):
        return u'%s %s' % (self.要引用的路面类型.路面类型, self.损坏类型)


class 道路等级(models.Model):
    道路等级 = models.CharField(verbose_name='道路等级', primary_key=True, max_length=4, choices=(
        ('1', '一级'), ('2', '二级'), ('3', '三级'), ('4', '四级')))
    备注 = models.CharField(verbose_name='备注', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = '道路等级'
        verbose_name = '道路等级'

    def __unicode__(self):
        return self.get_道路等级_display()

    def __str__(self):
        return self.get_道路等级_display()


# Create your models here.
class 道路基本档案(models.Model):
    道路编号 = models.CharField('道路编号', primary_key=True, max_length=100)
    # 车行道 = models.OneToOneField(车行道, on_delete=models.CASCADE)
    道路等级 = models.ForeignKey(道路等级, on_delete=models.CASCADE, verbose_name='道路等级', default='1', null=False)
    道路名称 = models.CharField('道路名称', max_length=100, null=False)

    经度 = models.FloatField('经度', null=True)
    纬度 = models.FloatField('纬度', null=True)

    路面等级 = models.CharField('路面等级', max_length=10, null=True)
    道路走向 = models.CharField('道路走向', max_length=100, null=True)
    起点 = models.CharField('起点', max_length=100, null=True)
    终点 = models.CharField('终点', max_length=100, null=True)
    设计单位 = models.CharField('设计单位', max_length=100, null=True)
    施工单位 = models.CharField('施工单位', max_length=100, null=True)
    设计时速 = models.IntegerField('设计时速', null=True)
    路幅宽度范围 = models.CharField('路幅宽度范围', max_length=100, null=True)
    道路长度 = models.FloatField('道路长度', null=True)
    道路面积 = models.FloatField('道路面积', null=True)
    AADT = models.FloatField('AADT', null=True)
    交通量等级 = models.CharField('交通量等级', max_length=4, null=True)
    所属乡镇 = models.CharField('所属乡镇', max_length=100, null=True)
    管理分类 = models.CharField('管理分类', max_length=50, null=True)
    管理单位 = models.CharField('管理单位', max_length=50, null=True)
    养护单位 = models.CharField('养护单位', max_length=50, null=True)
    建造年月 = models.DateField('建造年月', null=True)

    class Meta:
        verbose_name_plural = '道路基本档案'
        verbose_name = '道路基本档案'

    def __str__(self):
        return self.道路编号 + '  ' + self.道路名称

    def getDict(self):
        return {
            'roadId': self.道路编号,
            'roadName': self.道路名称,
            'roadLevel': self.道路等级.道路等级,
            'latlng': [self.纬度, self.经度]
        }

    def getLatlng(self):
        return [self.纬度, self.经度]


class RoadForm(ModelForm):
    class Meta:
        model = 道路基本档案
        fields = ['道路编号', '道路名称', '道路等级']


class 车行道(models.Model):
    车行道编号 = models.AutoField('车行道编号', primary_key=True)
    道路编号 = models.OneToOneField(道路基本档案, on_delete=models.CASCADE)
    路面类型 = models.ForeignKey(路面类型, on_delete=models.CASCADE, verbose_name='路面类型', default='1')
    基层类型 = models.CharField('基层类型', max_length=12, null=True)
    基层厚度 = models.FloatField('基层厚度', null=True)
    车道数 = models.IntegerField('车道数', null=True)
    通行方向 = models.CharField('通行方向', max_length=20, null=True)
    机动车道宽度范围 = models.CharField('机动车道宽度范围', max_length=100, null=True)
    左侧非机动车道宽度范围 = models.CharField('左侧非机动车道宽度范围', max_length=100, null=True)
    右侧非机动车道宽度范围 = models.CharField('右侧非机动车道宽度范围', max_length=100, null=True)
    车行道面积 = models.FloatField('车行道面积', null=True)
    有无公交车专用道 = models.CharField('有无公交车专用道', max_length=4, null=True)
    侧石类型 = models.CharField('侧石类型', max_length=12, null=True)
    侧石长度 = models.FloatField('侧石长度', null=True)
    平石类型 = models.CharField('平石类型', max_length=12, null=True)
    平石长度 = models.FloatField('平石长度', null=True)

    class Meta:
        verbose_name_plural = '道路的车行道档案'
        verbose_name = '道路的车行道档案'

    def __unicode__(self):
        return '道路编号:%s 车行道编号:%s' % (self.道路编号.道路编号, self.车行道编号)

    def __str__(self):
        return '道路编号:%s 车行道编号:%s' % (self.道路编号.道路编号, self.车行道编号)


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
        return self.工号 + ' ' + self.姓名

    def __str__(self):
        return self.工号 + ' ' + self.姓名

    class Meta:
        verbose_name = '职工'
        verbose_name_plural = '职工'


class 路面损坏单项扣分表(models.Model):
    损坏单项扣分编号 = models.AutoField('损坏单项扣分编号', primary_key=True)
    损坏类型 = models.ForeignKey(路面损坏类型, on_delete=models.CASCADE, verbose_name='损坏类型', default='1')
    扣分分值 = models.IntegerField('扣分分值', null=False)
    损坏密度 = models.IntegerField('损坏密度', default=0, null=False)

    class Meta:
        verbose_name = '路面损坏单项扣分表'
        verbose_name_plural = '路面损坏单项扣分表'


class 道路技术状况评价年报表(models.Model):
    道路编号 = models.ForeignKey(道路基本档案, on_delete=models.CASCADE, verbose_name='道路编号', null=True)
    评价日期 = models.DateField(verbose_name='评价日期', null=False)

    PQI = models.FloatField(verbose_name='PQI', null=False)
    PQI等级 = models.CharField(verbose_name='PQI等级', max_length=2, null=False,
                             choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', "D")))

    RQI = models.FloatField(verbose_name='RQI', null=False)
    RQI等级 = models.CharField(verbose_name='RQI等级', null=False, max_length=2,
                             choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', "D")))

    PCI = models.FloatField(verbose_name='PCI', null=False)
    PCI等级 = models.CharField(verbose_name='PCI等级', null=False, max_length=2,
                             choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', "D")))

    class Meta:
        verbose_name = '道路技术状况评价年报'
        verbose_name_plural = '道路技术状况评价年报'
