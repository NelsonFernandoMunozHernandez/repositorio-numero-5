from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_pedido, name='nuevo_pedido'),          # Crear un nuevo pedido
    path('historial/', views.historial_pedidos, name='historial_pedidos'),  # Ver el historial de pedidos
]