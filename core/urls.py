from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('success/', views.login_success_view, name='success')
] 
