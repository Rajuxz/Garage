# Generated by Django 5.1.1 on 2024-09-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_usermodel_options_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='latitude',
            field=models.FloatField(default=0.0, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='longitude',
            field=models.FloatField(default=0.0, verbose_name='Longitude'),
        ),
    ]
