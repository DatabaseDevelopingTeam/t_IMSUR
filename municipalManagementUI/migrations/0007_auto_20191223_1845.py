# Generated by Django 3.0 on 2019-12-23 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0006_auto_20191223_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='路面损坏类型',
            old_name='路面类型外键',
            new_name='要引用的路面类型',
        ),
    ]