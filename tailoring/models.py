from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class Appointment(models.Model):
    """
    Defines the Appointment Model
    """
    CONSULTATION = 'CON'
    DETAILS = 'DD'
    FABRICS = 'FAB'
    FIRST = 'FF'
    SECOND = 'SF'
    PICKUP = 'PU'
    AM1 = 'AM1'
    AM4 = 'AM4'
    PM1 = 'PM1'
    PM2 = 'PM2'
    PM3 = 'PM3'

    TYPE_CHOICES = [
        (CONSULTATION, 'Consultation'),
        (DETAILS, 'Details & Design'),
        (FABRICS, 'Fabrics'),
        (FIRST, 'First Fitting'),
        (SECOND, 'Second Fitting'),
        (PICKUP, 'Pick-up')
    ]
    TIME_CHOICES = [
        (AM1, '8:30 AM'),
        (AM4, '11:30 AM'),
        (PM1, '4:00 PM'),
        (PM2, '5:00 PM'),
        (PM3, '6:00 PM')
    ]

    user = models.ForeignKey(
        User, related_name='appointment', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=15, choices=TYPE_CHOICES, default='CONSULTATION')
    date = models.DateField()
    time = models.CharField(
        max_length=8, choices=TIME_CHOICES, default='AM1')
    comments = models.TextField()
    submitted = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
