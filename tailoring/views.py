from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from .models import Appointment
from .forms import AppointmentForm


class Home(View):
    """
    Handles traffic from the Homepage of the Website
    """
    def get(self, request):
        return render(request, 'home.html', {'title': 'Home'})


class About(View):
    """
    Handles the About Page
    """
    def get(self, request):
        return render(request, 'about.html', {'title': 'About'})


class Services(View):
    """
    Handles the Services Page
    """
    def get(self, request):
        return render(request, 'services.html', {'title': 'Services'})


class AppointmentList(LoginRequiredMixin, ListView):
    """
    Defines the logic for the User's Appointments page
    """
    model = Appointment
    context_object_name = 'appointments'

    def get_queryset(self):
        """
        Returns objects that belong to the current user
        """
        return Appointment.objects.filter(user=self.request.user)


class AppointmentDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    Defines the logic for each appointment
    """
    model = Appointment

    def test_func(self):
        """
        UserPassesTestMixin runs this method to check if user
        is the user who created the appointment
        """
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False


class AppointmentCreate(LoginRequiredMixin, CreateView):
    """
    Defines the logic for the AppointmentForm
    """
    model = Appointment
    form_class = AppointmentForm

    def form_valid(self, form):
        """
        Adds the logged in user before form is submitted
        """
        form.instance.user = self.request.user
        messages.success(self.request,
                         'Your appointment has been created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Overrides the form_invalid method to add error alerts
        """
        messages.error(self.request,
                       'Sorry an error occurred while creating your '
                       'appointment. Please try again!')
        return super().form_invalid(form)


class AppointmentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Defines the logic for the Update AppointmentForm
    """
    model = Appointment
    form_class = AppointmentForm
    template_name = 'tailoring/appointment_update.html'

    def form_valid(self, form):
        """
        Adds the logged in user before form is submitted
        """
        form.instance.user = self.request.user
        messages.success(self.request,
                         'Your appointment has been updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Overrides the form_invalid method to add error alerts
        """
        messages.error(self.request,
                       'Sorry an error occurred while updating your '
                       'appointment. Please try again!')
        return super().form_invalid(form)

    def test_func(self):
        """
        UserPassesTestMixin runs this method to check if the current
        logged in user matches the user who created the appointment
        """
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False


class AppointmentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Handles the logic for deleting posts
    """
    model = Appointment
    success_url = reverse_lazy('appointments')

    def test_func(self):
        """
        UserPassesTestMixin runs this method to check if the current
        logged in user matches the user who created the appointment
        """
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        """
        Dispays an alert on successful deletion
        """
        messages.success(self.request,
                         'Your appointment has been deleted.')
        return super(AppointmentDelete, self).delete(request, *args, **kwargs)
