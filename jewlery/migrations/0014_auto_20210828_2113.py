# Generated by Django 3.2 on 2021-08-28 16:43

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('jewlery', '0013_auto_20210818_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewlerymodel',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='jdatetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 28, 21, 13, 30, 170870)),
        ),
    ]
