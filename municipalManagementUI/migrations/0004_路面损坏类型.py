# Generated by Django 3.0 on 2019-12-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipalManagementUI', '0003_路面类型_车行道'),
    ]

    operations = [
        migrations.CreateModel(
            name='路面损坏类型',
            fields=[
                ('损坏类型', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='损坏类型')),
                ('路面类型外键', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='路面类型外键', to='municipalManagementUI.路面类型')),
            ],
        ),
    ]
