from django.contrib import admin
from .models import Tarea

admin.site.register(Tarea) #Se encarga de reconocer a la clase Tarea y hacerla presente en la ventana de admin
