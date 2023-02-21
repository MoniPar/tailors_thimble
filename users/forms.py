from django import forms
from allauth.account.forms import SignupForm
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from .models import Profile


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
                        max_length=16,
                        required=True,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control'}
                        )
    )
    event = forms.CharField(
                        max_length=50,
                        required=True,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control'}
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
                                   'rows': 4}
                        )
    )

    class Meta:
        model = Profile
        fields = ['phone', 'event', 'event_date', 'outfit_type']
