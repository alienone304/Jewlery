# Generated by Django 3.2 on 2021-07-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonusermodel',
            name='is_jewler_request',
            field=models.BooleanField(default=False, verbose_name='Jewler Request'),
        ),
    ]
