from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Defines the Profile Model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=16)
    event = models.CharField(max_length=50)
    event_date = models.DateField(null=True)
    outfit_type = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Profile Model
        """
        return f"{self.user.username}"
