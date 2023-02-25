from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home.as_view(), name='home-page'),
     path('appointments/', views.AppointmentList.as_view(),
          name='appointments'),
     path('appointments/<int:pk>/', views.AppointmentDetail.as_view(),
          name='appointment-detail'),
     path('appointments/new', views.AppointmentCreate.as_view(),
          name='appointment-create'),
     path('appointments/<int:pk>/update', views.AppointmentUpdate.as_view(),
          name='appointment-update'),
     path('appointments/<int:pk>/delete', views.AppointmentDelete.as_view(),
          name='appointment-delete'),
     path('about/', views.About.as_view(), name='about-page'),
     path('services/', views.Services.as_view(), name='services-page'),
]
