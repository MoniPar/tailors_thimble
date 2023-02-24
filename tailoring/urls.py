from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home-page'),
    path('appointments/', views.AppointmentList.as_view(),
         name='appointments'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(),
         name='appointment-detail'),
    path('about/', views.About.as_view(), name='about-page'),
    path('services/', views.Services.as_view(), name='services-page'),
]
