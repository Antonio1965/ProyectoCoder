from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(resquest):
  return HttpResponse("visita inicio")

def cursos(resquest):
  return HttpResponse("vista cursos")

def profesores(resquest):
  return HttpResponse("vistaprofesores")

def estudiantes(resquest):
  return HttpResponse("vista estudiantes")

def entregables(resquest):
  return HttpResponse("vistaentregables")