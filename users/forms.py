from django import forms
from allauth.account.forms import SignupForm
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from .models import Profile
import datetime


class CustomSignupForm(SignupForm):
    """
    Extends the default allauth SignupForm by adding custom fields.
    """
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
    first_name = forms.CharField(
        max_length=30, label='First Name:',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, label='Last Name:',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    """
    Interacts with the Profile model to let users update
    their profile information.
    """
    phone = forms.CharField(
                        min_length=12,
                        max_length=15,
                        required=True,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'pattern': '^[+][0-9]+',
                                   'placeholder': '+xxxxxxxxxxx',
                                   'title': 'Country code followed by phone'
                                            ' number'}
                        )
    )
    event = forms.CharField(
                        max_length=50,
                        required=True,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'placeholder': 'E.g. Wedding',
                                   'title': 'The type of event you need the'
                                   ' outfit for'}
                        )
    )
    event_date = forms.DateField(
                        required=True,
                        widget=NumberInput(
                            attrs={'class': 'form-control',
                                   'type': 'date'}
                        )
    )
    outfit_type = forms.CharField(
                        required=True,
                        widget=forms.Textarea(
                            attrs={'class': 'form-control',
                                   'rows': 4,
                                   'placeholder': 'Examples: Bridal Gown, '
                                   'Mother of the Bride, 3x Bridesmaids',
                                   'title': 'The type of outfit/s you are '
                                   'looking to have done'}
                        )
    )

    def clean_event_date(self):
        """
        Validation for the event_date
        """
        date = self.cleaned_data['event_date']
        # Only dates from today are accepted
        if date < date.today():
            raise forms.ValidationError("Your date is in the past!")
        # Only dates at least 30 days from today are accepted
        if date <= date.today() + datetime.timedelta(days=30):
            raise forms.ValidationError("Sorry your event date is sooner than"
                                        " our 30-day minimum window!")
        return date

    class Meta:
        model = Profile
        fields = ['phone', 'event', 'event_date', 'outfit_type']
