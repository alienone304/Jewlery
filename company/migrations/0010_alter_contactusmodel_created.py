# Generated by Django 3.2 on 2021-08-12 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_contactusmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 14, 45, 19, 929597, tzinfo=utc)),
        ),
    ]
