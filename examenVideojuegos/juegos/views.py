from django.shortcuts import render
from django.db.models import Avg
from .models import *

def index(request):
    return render(request, 'index.html')

def ejercicio1(request):
    juegos = Videojuego.objects.select_related('estudio_desarrollo')\
        .prefetch_related('plataformas')\
        .filter(titulo__icontains='Fantasy', estudio_desarrollo__sede__pais__icontains='Unidos')
    return render(request, 'ej1.html', {'juegos': juegos})

def ejercicio2(request):
    juegos = Videojuego.objects.select_related('estudio_desarrollo')\
        .prefetch_related('plataformas', 'analisis_set')\
        .filter(plataformas__fabricante__icontains='Sony', analisis__puntuacion__gt=75)[:3]
    return render(request, 'ej2.html', {'juegos': juegos})

def ejercicio3(request):
    juegos = Videojuego.objects.select_related('estudio_desarrollo')\
        .filter(videjuegoplataforma__isnull=True).order_by('-ventas_estimadas')
    return render(request, 'ej3.html', {'juegos': juegos})

def ejercicio4(request, anio):
    estudios = Estudio.objects.filter(videojuego__analisis__fecha__year=anio)\
        .order_by('-videojuego__analisis__puntuacion').distinct()
    return render(request, 'ej4.html', {'estudios': estudios, 'anio': anio})

def ejercicio5(request, estudio_nombre):
    juegos = Videojuego.objects.filter(estudio_desarrollo__nombre__icontains=estudio_nombre)\
        .annotate(media=Avg('analisis__puntuacion')).filter(media__gt=7.5)
    return render(request, 'ej5.html', {'juegos': juegos, 'estudio': estudio_nombre})

def ejercicio6(request, critico_nombre, fabricante, pais):
    analisis = Analisis.objects.select_related('videojuego', 'critico', 'videojuego__estudio_desarrollo')\
        .filter(
            critico__nombre__icontains=critico_nombre,
            videojuego__plataformas__fabricante__icontains=fabricante,
            videojuego__estudio_desarrollo__sede__pais__icontains=pais
        ).order_by('-fecha').first()
    return render(request, 'ej6.html', {'analisis': analisis})
