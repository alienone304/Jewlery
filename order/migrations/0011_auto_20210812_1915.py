# Generated by Django 3.2 on 2021-08-12 14:45

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_ordermodel_jdatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='jdatetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 12, 19, 15, 19, 921582)),
        ),
    ]
