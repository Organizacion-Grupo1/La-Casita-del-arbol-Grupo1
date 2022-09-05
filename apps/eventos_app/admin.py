from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Evento
from apps.eventos_app import models

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'img')
    search_fields = ('titulo', 'autor', 'creado')
    list_per_page = 25

    readonly_fields = ['evento_img']

    def evento_img(self,obj):
        return mark_safe('<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url))

admin.site.register(Evento, EventosAdmin)

'''
class ComentariosAdmin(admin.ModelAdmin):
    list_display=('autor', 'cuerpo_comentario','evento','creado','aprobado')

    list_filter = ('aprobado', 'creado')

    search_fields = ('autor', 'cuerpo_comentario')

    actions= ['aprobar_comentarios']

    def aprobar_comentarios(self,request,queryset):
        queryset.update(aprobado=True)

admin.site.register(Comentario,ComentariosAdmin)
'''