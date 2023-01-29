from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('inicio', inicio),
    path("cursos", cursos, name="Cursos"),
    path("profesores", profesores),
    path("estudiantes", estudiantes),
    path("entregables", entregables),
    path("agregar_flia", agregar_familia),
]