from django.urls import path
from . import views


HANDLER400 = 'juegos.views_errores.error_400'
HANDLER402 = 'juegos.views_errores.error_402'
HANDLER403 = 'juegos.views_errores.error_403'
HANDLER404 = 'juegos.views_errores.error_404'
HANDLER500 = 'juegos.views_errores.error_500'


urlpatterns = [
    path('', views.index, name='index'),
    path('ej1/', views.ejercicio1, name='ej1'),
    path('ej2/', views.ejercicio2, name='ej2'),
    path('ej3/', views.ejercicio3, name='ej3'),
    path('ej4/<int:anio>/', views.ejercicio4, name='ej4'),
    path('ej5/<str:estudio_nombre>/', views.ejercicio5, name='ej5'),
    path('ej6/<str:critico_nombre>/<str:fabricante>/<str:pais>/', views.ejercicio6, name='ej6'),
]

