from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_menu, name='listado_menu'),  # Muestra el menú
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # Muestra detalles de un producto específico
]