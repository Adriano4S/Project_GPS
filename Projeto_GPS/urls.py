from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP_GPS.urls')),
    path('APP_GPS/', include('APP_GPS.urls'))
]
