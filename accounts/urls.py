# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.guest_login, name='login'), # New login path for guests
]