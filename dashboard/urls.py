# D:\Django\Corelytix\dashboard\urls.py

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('server_list/', views.server_list_view, name='server_list'),
    path('clients/', views.client_list_view, name='client_list'),
]