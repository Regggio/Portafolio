from django.shortcuts import render, redirect
from django.views.generic.list import ListView #Representa a una lista de objetos
from django.views.generic.detail import DetailView #Se utiliza para darle estilo a mi lista
from django.views.generic.edit import CreateView, UpdateView, DeleteView #Se utiliza para que el usuario pueda a/m/d tareas desde la pagina principal
from django.views.generic.edit import FormView #Se utiliza para crear le Registro
from django.contrib.auth.forms import UserCreationForm #Se utiliza para crear le Registro
from django.contrib.auth import login
from django.contrib.auth.views import LoginView #Se utiliza para crear el formulario de Logueo y Deslogeo
from django.contrib.auth.mixins import LoginRequiredMixin #La utilizamos para restringir el acceso a nuestras vistas
from django.urls import reverse_lazy #Se utiliza para que cuando se termine una accion nos reedireccione a otro lugar en especifico
from .models import Tarea

class Logueo(LoginView):
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True #Parametro que define si se redirige a un usuario ya autenticado

    def get_success_url(self): #Sobreescribimos el metodo get_success_url
        return reverse_lazy('tareas')

class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    def form_valid(self, form): #El metodo hace que una vez registrado ya se logee ese mimso usuario en la pagina
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro,self).form_valid(form)

    def get(self,*args,**kwargs): #Soobreescribimos el metodo para que el usuario no pueda entrar a la pagina de registro si ya esta logeado
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro,self).get(*args,**kwargs)

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea #El modelo del que se basara mi lista de pendientes
    context_object_name = 'tareas' #Es una forma distinta de referirse al objeto

    def get_context_data(self, **kwargs): #Sobrescribimos el metodo para que los usuarios solo puedan ver sus tareas
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario = self.request.user, completo = False) #Hacemos que las tareas mostradas sean solo aquellas propias del usuario en sesion
        context['count'] = context['tareas'].count() #Me muestra unicamente las taras incompletas

        #Si se realiza una busqueda solo muestra las tareas que contengan la tareas buscada
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains = valor_buscado)
        context['valor_buscado'] =  valor_buscado
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas') #Vuelve a la pagina original cuando se crea un formulario correctamente

    def form_valid(self, form):
        form.instance.usuario = self.request.user #Hace que la tarea se asocie al usuario que la esta creando
        return super(CrearTarea,self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')



