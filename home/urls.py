from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]