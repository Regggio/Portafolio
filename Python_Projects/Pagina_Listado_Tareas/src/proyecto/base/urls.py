from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',ListaPendientes.as_view(), name = 'tareas'),#El metodo as_view es necesario ya que urls no soporta clases
               path('login/', Logueo.as_view(), name = 'login'),
               path("logout/",LogoutView.as_view(next_page = 'login'), name = 'logout'), #Next_page es a donde va a mandar al usuario si se realiza el logout
               path('registro/',PaginaRegistro.as_view(), name = 'registro'),
               path('tarea/<int:pk>',DetalleTarea.as_view(), name = 'tarea'), #El primer campo de path es para decir que de la pagina prinicpal/tarea/num_tarea va a estar la view
               path('crear-tarea/',CrearTarea.as_view(), name = 'crear-tarea'),
               path('editar-tarea/<int:pk>',EditarTarea.as_view(), name = 'editar-tarea'),
               path('eliminar-tarea/<int:pk>',EliminarTarea.as_view(), name = 'eliminar-tarea')]

