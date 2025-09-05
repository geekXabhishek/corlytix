# D:\Django\Corelytix\corelytix\urls.py

from django.contrib import admin
from django.urls import path, include # 'include' को import करना ज़रूरी है

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    
    # यह लाइन dashboard ऐप के सभी URLs को शामिल करती है
    path('', include('dashboard.urls')), 
]
=======
    path('', include('core.urls')),
    path('', include('serverlist.urls'))
]
>>>>>>> 89f89b1 (Initial commit)
