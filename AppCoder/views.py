from django.shortcuts import render, HttpResponse

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