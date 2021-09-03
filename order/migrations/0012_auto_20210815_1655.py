# Generated by Django 3.2 on 2021-08-15 12:25

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20210812_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='sale_wage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='jdatetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 15, 16, 55, 20, 775638)),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
