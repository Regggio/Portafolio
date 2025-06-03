from django.db import models
from django.contrib.auth.models import User

# En este archivo creamos la estructura de la lista de pendientes (BBDD)
class Tarea(models.Model): #Como queremos que sea un modelo para trabajar con el debe heredar del mismo
    usuario = models.ForeignKey(User, #Esto dice que la clave foranea de usarios responde a la clase User
                                on_delete = models.CASCADE, #Esto hace que se borren todas las tareas asociadas al usario si se borra el mismo
                                null = True, #Se permite vacios en este campo
                                blank = True) #Permite que si se crea un formulario este mismo este vacio
    titulo = models.CharField(max_length = 200) #Esto hace que nuestro campo titulo sea un campo alfanumerico de maximo 200 carac
    descripcion = models.TextField(null = True,
                                   blank = True)
    completo = models.BooleanField(default = False)
    creado = models.DateTimeField(auto_now_add = True) #Esto dice que cuando se cree el objeto esete campo tenga la fecha y hora de la creacion del mismo

    def __str__(self): #Funcion que define que se muestra cuando se hace un printf del objeto
        return self.titulo

    class Meta: #Clase creada para definir el orden en el que se muestran nuestros datos
        ordering = ['completo']
#Luego de crear esta clase hago python manage.py makemigrations para dejar plasmado en un archivo a mi tabla