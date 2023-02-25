from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from .models import Appointment
from .constants import TYPE_CHOICES, TIME_CHOICES


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

    class Meta:
        model = Appointment
        fields = ['type', 'date', 'time', 'comments']
