# Generated by Django 3.0 on 2019-12-23 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0004_路面损坏类型'),
    ]

    operations = [
        migrations.AlterField(
            model_name='路面损坏类型',
            name='路面类型外键',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn路面类型', to='municipalManagementUI.路面类型'),
        ),
    ]