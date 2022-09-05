from time import timezone
from django.shortcuts import render, redirect
from apps.eventos_app.models import Evento
from apps.noticias_app.models import Noticia,Categoria,Comentarios
from django.http.response import Http404
from django.conf import settings
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from .forms import NoticiaForm, CommentarioForm      # NUEVO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)
from django.shortcuts import render #NUEVO

'''
def eventos(request):
    return render(request, "ProyectoWebApp/eventos.html")
'''


def eventos(request):
    lista_eventos = Evento.objects.all().order_by('creado')
    context = {
        "eventos": lista_eventos,
        "MEDIA_ROOT": 'media/img/eventos/'}
    return render(request, 'eventos.html',context) # NUEVO