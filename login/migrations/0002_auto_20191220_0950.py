# Generated by Django 3.0 on 2019-12-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='职工',
            name='ticket',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ticket'),
        ),
    ]
