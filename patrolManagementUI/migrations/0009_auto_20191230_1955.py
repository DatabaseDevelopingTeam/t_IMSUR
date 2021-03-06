# Generated by Django 3.0 on 2019-12-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrolManagementUI', '0008_auto_20191230_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='日常巡查损害记录',
            name='路面类型',
        ),
        migrations.AddField(
            model_name='日常巡查损害记录',
            name='备注',
            field=models.CharField(default=' ', max_length=100, verbose_name='备注'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='定期检测记录',
            name='定期检查记录编号',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='日常巡查损害记录',
            name='日常巡查损害记录编号',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='日常巡查记录',
            name='日常巡查记录编号',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='路面定期检查损害记录',
            name='定期巡察损害记录编号',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='路面平整度检测记录',
            name='备注',
            field=models.CharField(max_length=100, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='路面平整度检测记录',
            name='平整度检测记录编号',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
    ]
