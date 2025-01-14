from django.urls import path
from .views import telemetry_dashboard

urlpatterns = [
    path('', telemetry_dashboard, name='telemetry_dashboard'),
]
