from django.urls import path, include
from travelApp.views import home

urlpatterns = [
    path('home/',home),
]
