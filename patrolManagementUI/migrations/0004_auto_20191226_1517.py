# Generated by Django 3.0 on 2019-12-26 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0010_道路等级_备注'),
        ('patrolManagementUI', '0003_auto_20191223_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='日常巡查',
            name='道路基本档案',
        ),
        migrations.AddField(
            model_name='日常巡查',
            name='道路名称',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='municipalManagementUI.道路基本档案'),
        ),
        migrations.AddField(
            model_name='日常巡查',
            name='道路编号',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='no', to='municipalManagementUI.道路基本档案'),
        ),
    ]