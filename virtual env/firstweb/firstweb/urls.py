
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('webapp/',include('webapp.urls')),
    
]
