# Generated by Django 3.0 on 2019-12-30 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0013_auto_20191229_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='道路技术状况评价年报表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('评价日期', models.DateField(verbose_name='评价日期')),
                ('PQI', models.FloatField(verbose_name='PQI')),
                ('PQI等级', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, verbose_name='PQI等级')),
                ('RQI', models.FloatField(verbose_name='RQI')),
                ('RQI等级', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, verbose_name='RQI等级')),
                ('PCI', models.FloatField(verbose_name='PCI')),
                ('PCI等级', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, verbose_name='PCI等级')),
                ('道路编号', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='municipalManagementUI.道路基本档案', verbose_name='道路编号')),
            ],
            options={
                'verbose_name': '道路技术状况评价年报',
                'verbose_name_plural': '道路技术状况评价年报',
            },
        ),
    ]
