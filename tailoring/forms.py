from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from .models import Appointment
from .constants import TYPE_CHOICES, TIME_CHOICES
from datetime import date


class AppointmentForm(ModelForm):
    """
    Interacts with the Appointment model to let users
    create an appointment
    """
    type = forms.ChoiceField(
                required=True,
                choices=TYPE_CHOICES,
                widget=forms.Select(
                    attrs={'class': 'form-control'}
                )
            )
    date = forms.DateField(
                required=True,
                widget=NumberInput(
                    attrs={'class': 'form-control',
                           'type': 'date'}
                )
            )
    time = forms.ChoiceField(
                required=True,
                choices=TIME_CHOICES,
                widget=forms.Select(
                    attrs={'class': 'form-control'}
                )
            )
    comments = forms.CharField(
                    required=False,
                    max_length=150,
                    widget=forms.Textarea(
                        attrs={'class': 'form-control',
                               'rows': 4}
                    )
                )

    # adapted from https://tinyurl.com/sm6mu2bv
    def clean_date(self):
        """
        Validation for the date
        """
        date = self.cleaned_data['date']
        appointments_on_date = Appointment.objects.filter(date__exact=date)
        # Only dates from tomorrow are accepted
        if date <= date.today():
            raise forms.ValidationError("Please choose a date and time at"
                                        " least 24 hours from now.")
        # Monday and Sunday are not accepted
        if date.weekday() == 0 or date.weekday() == 6:
            raise forms.ValidationError("Sorry, we're only open Tuesday to"
                                        " Saturday.")
        # No more than 5 appointments per day are accepted
        if len(appointments_on_date) > 5:
            raise forms.ValidationError("There are no available appointments"
                                        " left on this day, please try again!")
        return date

    def clean_time(self):
        """
        Checks if date is valid and validates time
        """
        time = self.cleaned_data['time']
        # date needs to be valid first
        if 'date' not in self.cleaned_data:
            raise forms.ValidationError("Please choose a valid date first")
        date = self.cleaned_data['date']
        appointments_on_date = Appointment.objects.filter(date__exact=date)
        times = [a['time'] for a in appointments_on_date.values('time')]
        # time cannot be already in list of times for date selected
        if time in times:
            raise forms.ValidationError("Sorry, there is already an "
                                        "appointment booked for this time.")
        return time

    class Meta:
        model = Appointment
        fields = ['type', 'date', 'time', 'comments']
