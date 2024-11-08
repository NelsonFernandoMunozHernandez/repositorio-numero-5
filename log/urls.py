from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),   # Iniciar sesión
    path('logout/', views.user_logout, name='logout'), # Cerrar sesión
    path('register/', views.register, name='register'), # Registro de usuarios
]