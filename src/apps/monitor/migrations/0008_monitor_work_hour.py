# Generated by Django 3.1.2 on 2020-11-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_monitor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='work_hour',
            field=models.IntegerField(default=1, verbose_name='work_hours'),
        ),
    ]