"""blackpit URL Configuration
"""
from django.urls import path
from .views import index, vaccinated

urlpatterns = [
    path('', index, name='home'),
    path('vaccinated', vaccinated, name='vaccinated')
]
