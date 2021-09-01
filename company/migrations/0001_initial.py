# Generated by Django 3.2 on 2021-07-26 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=264, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=264, null=True)),
                ('request', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 7, 26, 15, 2, 56, 241029, tzinfo=utc))),
            ],
        ),
    ]
