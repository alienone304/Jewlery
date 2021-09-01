# Generated by Django 3.2 on 2021-07-22 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewlery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JewleryPictureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='jewlery/pictures')),
                ('jewlery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='jewlery.jewlerymodel')),
            ],
        ),
    ]
