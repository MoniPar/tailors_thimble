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
        Checks and throws an error if date is in the past
        """
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Appointment
        fields = ['type', 'date', 'time', 'comments']
