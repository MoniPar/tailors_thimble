from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    """
    Represents the Appointment Model in the Admin interface
    """
    list_display = (
        'user', 'type', 'date', 'time',
        'comments', 'submitted', 'approved'
    )
    list_filter = (
        'date', 'type', 'approved'
    )
    search_fields = ('user_username', 'type', 'date')
    actions = ['approve_appointments']

    def approve_appointments(self, request, queryset):
        """
        Adds the approval action to the actions drop-down list
        """
        queryset.update(approved=True)
