"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.urls import path, include
from django.urls import include, path  #(VER SI ESTA CORRECTO EL DE ARRIBA)
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from apps.noticias_app import views # Agregue la vista de la App
from ProyectoWebApp import views # Agregue la vista de la App
from apps.eventos_app import views # Agregue la vista de la App

urlpatterns = [
    path('admin/', admin.site.urls),

    path('blog/', include('blog.urls')),
    
    path('', include('ProyectoWebApp.urls')),

    path('noticias/', include('apps.noticias_app.urls')),
        
    url('noticias/', include('apps.noticias_app.urls')),

    path('eventos/', include('apps.eventos_app.urls')),  # NUEVO
        
    url('eventos/', include('apps.eventos_app.urls')),   # NUEVO

    # Esta opcion sirve para?? path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT, show_indexes=True)
    