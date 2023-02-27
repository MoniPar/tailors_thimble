# Generated by Django 3.2.18 on 2023-02-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailoring', '0004_auto_20230225_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('AM1', '8:30 AM'), ('AM4', '11:30 AM'), ('PM1', '4:00 PM'), ('PM2', '5:00 PM'), ('PM3', '6:00 PM')], default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='type',
            field=models.CharField(choices=[('CON', 'Consultation'), ('DD', 'Details & Design'), ('FAB', 'Fabrics'), ('FF', 'First Fitting'), ('SF', 'Second Fitting'), ('PU', 'Pick-up')], default='', max_length=15),
        ),
    ]