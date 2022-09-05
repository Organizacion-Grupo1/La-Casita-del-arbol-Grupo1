

from django.contrib import admin
from django.urls import include,path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.eventos_app import views
from django.urls import path


#from django.urls import path 


urlpatterns = [
    path('eventos',views.eventos, name="Eventos"),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)