from django.shortcuts import render
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
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
    ordering = ['submitted']
    paginate_by = 6


class AppointmentDetail(LoginRequiredMixin, DetailView):
    """
    Defines the logic for each appointment
    """
    model = Appointment


class AppointmentCreate(LoginRequiredMixin, CreateView):
    """
    Defines the logic for the appointment form
    """
    model = Appointment
    form_class = AppointmentForm

    def form_valid(self, form):
        """
        Adds the logged in user before form is submitted
        """
        form.instance.user = self.request.user

        return super().form_valid(form)
