from django.db import models

# Create your models here.


class 道路等级(models.Model):
    道路等级 = models.CharField('道路等级', primary_key=True, max_length=4)

class 路面类型(models.Model):
    路面类型 = models.CharField('路面类型', primary_key=True, max_length=12)

class 车行道(models.Model):
    车行道编号 = models.AutoField('车行道编号', primary_key=True)
    #道路编号 = models.OneToOneField(道路基本档案, on_delete=models.CASCADE)
    路面类型 = models.ForeignKey(路面类型, on_delete=models.CASCADE, verbose_name='路面类型', default='1')
    基层类型 = models.CharField('基层类型', max_length=12, null=False)
    基层厚度 = models.FloatField('基层厚度', null=False)
    车道数 = models.IntegerField('车道数', null=False)
    通行方向 = models.CharField('通行方向', max_length=20, null=False)
    机动车道宽度范围 = models.CharField('机动车道宽度范围', max_length=100, null=False)
    左侧非机动车道宽度范围 = models.CharField('左侧非机动车道宽度范围', max_length=100, null=False)
    右侧非机动车道宽度范围 = models.CharField('右侧非机动车道宽度范围', max_length=100, null=False)
    车行道面积 = models.FloatField('车行道面积', null=False)
    有无公交车专用道 = models.CharField('有无公交车专用道', max_length=4, null=False)
    侧石类型 = models.CharField('侧石类型', max_length=12, null=False)
    侧石长度 = models.FloatField('侧石长度', null=False)
    平石类型 = models.CharField('平石类型', max_length=12, null=False)
    平石长度 = models.FloatField('平石长度', null=False)

class 道路基本档案(models.Model):
    道路编号 = models.CharField('道路编号', primary_key=True, max_length=100)
    车行道编号 = models.OneToOneField(车行道, on_delete=models.CASCADE)
    道路等级 = models.ForeignKey(道路等级, on_delete=models.CASCADE, verbose_name='道路等级', default='1')
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

class 定期任务(models.Model):
    巡查日期=models.DateField('巡查日期')
    道路编号=models.ForeignKey(道路基本档案,verbose_name='巡查道路编号',related_name='roadNumber',on_delete=models.CASCADE)
    道路名称=models.ForeignKey(道路基本档案,verbose_name='巡查道路名称',on_delete=models.CASCADE,related_name='roadName')
    道路等级=models.ForeignKey(道路基本档案,verbose_name='巡查道路等级',on_delete=models.CASCADE,related_name='roadLevel')


    class Meta:
        verbose_name = '定期任务'
        verbose_name_plural = '定期任务'
