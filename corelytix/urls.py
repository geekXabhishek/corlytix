from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('serverlist.urls')),  # 👈 your new app
    path("__reload__/", include("django_browser_reload.urls")),  # only if using browser reload
]
