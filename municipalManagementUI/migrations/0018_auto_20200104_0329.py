# Generated by Django 3.0 on 2020-01-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0017_auto_20200104_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='路面损坏单项扣分表',
            name='损坏密度',
            field=models.IntegerField(default=0, verbose_name='损坏密度'),
        ),
    ]
