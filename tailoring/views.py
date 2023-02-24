from django.shortcuts import render
from django.views import View
from django.views.generic import (
    ListView, DetailView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from .models import Appointment


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


class AppointmentList(ListView):
    """
    Defines the logic for the User's Appointments page
    """
    model = Appointment
    context_object_name = 'appointments'
    ordering = ['submitted']
    paginate_by = 6


class AppointmentDetail(DetailView):
    """
    Defines the logic for each appointment
    """
    model = Appointment
    
