# Generated by Django 3.0 on 2019-12-23 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0006_auto_20191223_1244'),
        ('patrolManagementUI', '0002_auto_20191223_1137'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='定期任务',
            new_name='定期巡查',
        ),
        migrations.AlterModelOptions(
            name='定期巡查',
            options={'verbose_name': '定期巡查', 'verbose_name_plural': '定期巡查'},
        ),
        migrations.CreateModel(
            name='日常巡查',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('巡查日期', models.DateField(verbose_name='巡查日期')),
                ('道路基本档案', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='municipalManagementUI.道路基本档案')),
            ],
            options={
                'verbose_name': '日常巡查',
                'verbose_name_plural': '日常巡查',
            },
        ),
    ]