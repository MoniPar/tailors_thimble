from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.views import SignupView
from django.views.generic import View
from django.contrib import messages
from .forms import CustomSignupForm, UserProfileForm
from .models import Profile


class CustomSignupView(SignupView):
    """
    Defines the logic for the CustomSignupForm
    """
    template_name = 'signup.html'
    form_class = CustomSignupForm


class ProfileUpdateView(LoginRequiredMixin, View):
    """
    Defines the logic for the Profile Page
    """
    model = Profile
    template_name = 'users/profile.html'

    def get(self, request):
        """
        Creates the UserProfileForm object and
        passes it to the profile.html template
        """
        profile_form = UserProfileForm(instance=request.user.profile)

        context = {
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        """
        Creates the UserProfileForm object and
        passes additional data from request.POST
        """
        profile_form = UserProfileForm(request.POST,
                                       instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            username = request.user.username

            messages.success(request,
                             f"{username}, Your profile has been"
                             " updated successfully!")

            return redirect('/')
        else:
            context = {
                'profile_form': profile_form
            }
            messages.error(request,
                           'An error has occurred while updating'
                           'your profile. Please try again!')

            return render(request, self.template_name, context)
