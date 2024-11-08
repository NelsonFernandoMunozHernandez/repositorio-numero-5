from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),              # Muestra el perfil del usuario
    path('editar/', views.editar_perfil, name='editar_perfil'), # Edita el perfil del usuario
]