from django.shortcuts import render
from django.views import View


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
