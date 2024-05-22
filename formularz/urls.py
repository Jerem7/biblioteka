from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formularz/', include('formularz.urls')),  # Dodaj tę linię
]
