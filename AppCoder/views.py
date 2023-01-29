from django.shortcuts import render, HttpResponse
from AppCoder.models import Familiar

# Create your views here.
def inicio(resquest):
  return render(resquest, "AppCoder/inicio.html")

def cursos(resquest):
  return render(resquest,"AppCoder/verCursos.html")

def profesores(resquest):
  return render(resquest,"AppCoder/verProfesores.html")

def estudiantes(resquest):
  return render(resquest,"Appcoder/verEstudiantes.html")

def entregables(resquest):
  return render(resquest,"AppCoder/verEntregables.html")

def agregar_familia(resquest):
  familiar1 = Familiar(parentesco="hermano", nombre="Juan", edad= 54, fecha="1956-01-25")
  familiar1.save()
  
  return HttpResponse(f"Hemos agregado a la base de datos al familiar {familiar1.nombre}")