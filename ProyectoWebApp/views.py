from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    
#def noticias2(request):
#   return render(request, "ProyectoWebApp/noticias.html")

def eventos(request):
    return render(request, "ProyectoWebApp/eventos.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")

def login(request):
    return render(request, "ProyectoWebApp/login.html")
