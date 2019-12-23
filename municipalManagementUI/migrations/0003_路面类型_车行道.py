# Generated by Django 3.0 on 2019-12-23 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0002_道路基本档案_道路等级'),
    ]

    operations = [
        migrations.CreateModel(
            name='路面类型',
            fields=[
                ('路面类型', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='路面类型')),
            ],
        ),
        migrations.CreateModel(
            name='车行道',
            fields=[
                ('车行道编号', models.AutoField(primary_key=True, serialize=False, verbose_name='车行道编号')),
                ('基层类型', models.CharField(max_length=12, verbose_name='基层类型')),
                ('基层厚度', models.FloatField(verbose_name='基层厚度')),
                ('车道数', models.IntegerField(verbose_name='车道数')),
                ('通行方向', models.CharField(max_length=20, verbose_name='通行方向')),
                ('机动车道宽度范围', models.CharField(max_length=100, verbose_name='机动车道宽度范围')),
                ('左侧非机动车道宽度范围', models.CharField(max_length=100, verbose_name='左侧非机动车道宽度范围')),
                ('右侧非机动车道宽度范围', models.CharField(max_length=100, verbose_name='右侧非机动车道宽度范围')),
                ('车行道面积', models.FloatField(verbose_name='车行道面积')),
                ('有无公交车专用道', models.CharField(max_length=4, verbose_name='有无公交车专用道')),
                ('侧石类型', models.CharField(max_length=12, verbose_name='侧石类型')),
                ('侧石长度', models.FloatField(verbose_name='侧石长度')),
                ('平石类型', models.CharField(max_length=12, verbose_name='平石类型')),
                ('平石长度', models.FloatField(verbose_name='平石长度')),
                ('路面类型', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='municipalManagementUI.路面类型', verbose_name='路面类型')),
                ('道路编号', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='municipalManagementUI.道路基本档案')),
            ],
        ),
    ]
