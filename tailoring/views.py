from django.shortcuts import render
from django.views import View


class Home(View):
    """
    Handles the traffic from the Homepage of the Website
    """
    def get(self, request):
        return render(request, 'home.html', {'title': 'Home'})
