# Generated by Django 3.2 on 2021-08-07 15:05

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_ordermodel_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 7, 19, 35, 29, 722621)),
        ),
    ]