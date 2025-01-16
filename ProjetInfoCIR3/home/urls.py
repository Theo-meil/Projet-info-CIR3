from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('role_management/', views.role_management, name='role_management'),
    path('manage_matches/', views.manage_matches, name='manage_matches'),
]