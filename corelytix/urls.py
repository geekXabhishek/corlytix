# D:\Django\Corelytix\corelytix\urls.py

from django.contrib import admin
from django.urls import path, include # 'include' को import करना ज़रूरी है

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # यह लाइन dashboard ऐप के सभी URLs को शामिल करती है
    path('', include('dashboard.urls')), 


    path('core/', include('core.urls')),

]