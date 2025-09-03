# D:\Django\Corelytix\dashboard\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # डैशबोर्ड पेज का URL
    path('', views.dashboard_view, name='dashboard'),
    
    # सर्वर लिस्ट पेज का URL
    path('server_list/', views.server_list_view, name='server_list'),
    
    # क्लाइंट लिस्ट पेज का URL
    path('clients/', views.client_list_view, name='client_list'),
]