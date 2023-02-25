from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .constants import TYPE_CHOICES, TIME_CHOICES


class Appointment(models.Model):
    """
    Defines the Appointment Model
    """
    user = models.ForeignKey(
        User, related_name='appointment', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=15, choices=TYPE_CHOICES, default='Consultation')
    date = models.DateField()
    time = models.CharField(
        max_length=8, choices=TIME_CHOICES, default='8:30 AM')
    comments = models.TextField()
    submitted = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation
        """
        return f'{self.user}'

    def get_absolute_url(self):
        """
        Returns the full URL to the appointment route as a string
        """
        return reverse('appointments')
