# Generated by Django 3.0 on 2019-12-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrolManagementUI', '0004_auto_20191226_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='定期巡查',
            old_name='道路基本档案',
            new_name='巡查道路',
        ),
        migrations.RenameField(
            model_name='日常巡查',
            old_name='道路编号',
            new_name='巡查道路',
        ),
        migrations.RemoveField(
            model_name='日常巡查',
            name='道路名称',
        ),
        migrations.AddField(
            model_name='定期巡查',
            name='巡查状态',
            field=models.CharField(choices=[('1', '未巡查'), ('2', '已巡查')], default='未巡查', max_length=20,
                                   verbose_name='巡查状态'),
        ),
        migrations.AddField(
            model_name='日常巡查',
            name='巡查状态',
            field=models.CharField(choices=[('1', '未巡查'), ('2', '已巡查')], default='未巡查', max_length=20,
                                   verbose_name='巡查状态'),
        ),
    ]
