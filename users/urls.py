"""defines url patterns for the users app"""
from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns =[
    # including default auth urls
    path('', include('django.contrib.auth.urls')),

    # defining links for registration
    path('register/', views.register, name='register'),
]
