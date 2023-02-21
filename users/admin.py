from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Represents the Profile Model in the admin interface.
    """
    list_display = (
        'user', 'phone', 'event', 'event_date',
        'outfit_type'
    )
    list_filter = (
        'user__username', 'event', 'event_date'
    )
    search_fields = (
        'user__username', 'event_date'
    )
