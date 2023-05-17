from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:num>',views.tax),
    path('taxrate',views.rate),

    
]