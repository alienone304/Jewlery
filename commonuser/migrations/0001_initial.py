# Generated by Django 3.2 on 2021-07-13 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='commonusers', serialize=False, to='accounts.usermodel')),
                ('address', models.TextField(blank=True, null=True)),
                ('is_jeweler', models.BooleanField(default=False, verbose_name='Jewler Status')),
            ],
        ),
    ]
