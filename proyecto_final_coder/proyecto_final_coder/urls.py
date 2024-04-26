"""
URL configuration for proyecto_final_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from reserva_turnos.views import home_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("reserva_turnos/", include("reserva_turnos.urls")) # conecto las URLS de `reserva_turnos` con las URLS generales
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)