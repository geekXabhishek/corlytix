from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.server, name='server'),

    path("__reload__/", include("django_browser_reload.urls")),
]
