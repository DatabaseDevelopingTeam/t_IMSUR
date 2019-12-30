# Generated by Django 3.0 on 2019-12-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0012_auto_20191229_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='车行道',
            name='侧石类型',
            field=models.CharField(max_length=12, null=True, verbose_name='侧石类型'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='侧石长度',
            field=models.FloatField(null=True, verbose_name='侧石长度'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='右侧非机动车道宽度范围',
            field=models.CharField(max_length=100, null=True, verbose_name='右侧非机动车道宽度范围'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='基层厚度',
            field=models.FloatField(null=True, verbose_name='基层厚度'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='基层类型',
            field=models.CharField(max_length=12, null=True, verbose_name='基层类型'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='左侧非机动车道宽度范围',
            field=models.CharField(max_length=100, null=True, verbose_name='左侧非机动车道宽度范围'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='平石类型',
            field=models.CharField(max_length=12, null=True, verbose_name='平石类型'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='平石长度',
            field=models.FloatField(null=True, verbose_name='平石长度'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='有无公交车专用道',
            field=models.CharField(max_length=4, null=True, verbose_name='有无公交车专用道'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='机动车道宽度范围',
            field=models.CharField(max_length=100, null=True, verbose_name='机动车道宽度范围'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='车行道面积',
            field=models.FloatField(null=True, verbose_name='车行道面积'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='车道数',
            field=models.IntegerField(null=True, verbose_name='车道数'),
        ),
        migrations.AlterField(
            model_name='车行道',
            name='通行方向',
            field=models.CharField(max_length=20, null=True, verbose_name='通行方向'),
        ),
        migrations.AlterField(
            model_name='道路等级',
            name='备注',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
    ]
