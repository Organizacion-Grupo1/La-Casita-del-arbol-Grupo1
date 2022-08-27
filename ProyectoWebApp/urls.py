from django.urls import path

from ProyectoWebApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.home, name="Home"),
    path('noticias',views.noticias, name="Noticias"),
    path('eventos',views.eventos, name="Eventos"),
    path('contacto',views.contacto, name="Contacto"),
    path('login',views.login, name="login"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #este tenia de Bruno, pero le voy a poner el de la profe para probar si los errores de direcciones tienen que ver con este
