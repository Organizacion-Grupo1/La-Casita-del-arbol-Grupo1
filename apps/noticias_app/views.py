from time import timezone
from django.shortcuts import render, redirect
from apps.noticias_app.models import Noticia,Categoria,Comentarios
from django.http.response import Http404
from django.conf import settings
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm, CommentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)
from django.shortcuts import render # agregue ultimo

# Create your views here.

''' 
def noticias(request):
    noticias_app=Noticia, Categoria, Comentarios.objects.all()
    return render(request, "apps.noticias_app/noticias.html",{"noticias_app":noticias_app})
''' 
'''
def index(request):
    #texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = Noticia.objects.all().order_by('creado').reverse()[:3]
    context ={
        'noticiasdestacadas':ultimasnoticias
    }
    return render(request, 'index.html',context)
'''
'''
def nosotros(request):
    return render(request, 'nosotros.html',{})
'''

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
        #"MEDIA_ROOT": 'media/img/noticias/'
    }
    return render(request, 'noticias.html',context)


def noticiasdetalle(request,id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    form=CommentarioForm()
    if request.method=='POST':
        form = CommentarioForm(request.POST)
        if form.isvalid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["autor"])
            print("Comentario:" + form.cleaned_data["cuerpo_comentario"])
            comment = Comentarios(
                author=form.cleaned_data["autor"],
                comment_body=form.cleaned_data["cuerpo_comentario"],
                noticia=datanoticia
            )
            comment.save()

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios,
        # "formulario comentario": form,
        "MEDIA_ROOT": 'media/img/noticias/'
        
    }

    return render(request,'detalle-noticia.html',context)



'''
class CrearNoticiaView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    #redirect_field_name='index_detail.html'

    form_class = NoticiaForm

    model = Noticia


    def blog_categoria(request, categoria):
        posts = Noticia.objects.filter(
            categories__name__contains=categoria
        ).order_by(
            'creado'
        )
        context = {
            "categoria": categoria,
            "posts": posts
        }
        return render(request, "blog_categoria.html", context)
        
'''
@login_required
def post_publish(request, id):
    try:
        noticias =Noticia.objects.get(id =id)
    except Noticia.DoesNotExist:
        raise Http404('No existe la noticia seleccionada')
    
    Noticia.publish()
    return redirect('detalle-noticia', id=id)


@login_required
def comment_approve(request, id):
    try:
        comentarios =Comentarios.objects.get(id =id)
    except Comentarios.DoesNotExist:
        raise Http404('El comentario no existe')
    comentarios.approve()
    return redirect('detalle-noticia', id=comentarios.noticia.id)


@login_required
def comment_remove(request, id):
    try:
        comentario =Comentarios.objects.get(id =id)
    except Comentarios.DoesNotExist:
        raise Http404('El comentario no existe')
    noticia_id = comentario.noticia.id
    comentario.delete()
    return redirect('noticia_detalle', id=noticia_id)