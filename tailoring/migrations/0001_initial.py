# Generated by Django 3.2.18 on 2023-02-22 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CON', 'Consultation'), ('DD', 'Details & Design'), ('FAB', 'Fabrics'), ('FF', 'First Fitting'), ('SF', 'Second Fitting'), ('PU', 'Pick-up')], default='CONSULTATION', max_length=15)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('AM1', '8:30 AM'), ('AM4', '11:30 AM'), ('PM1', '4:00 PM'), ('PM2', '5:00 PM'), ('PM3', '6:00 PM')], default='AM1', max_length=8)),
                ('comments', models.TextField()),
                ('submitted', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
