# Generated by Django 5.1.1 on 2024-09-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_usermodel_latitude_alter_usermodel_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='Phone Number'),
        ),
    ]
