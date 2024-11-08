from django.shortcuts import render
from menu.models import Producto  # Importa el modelo de productos si ya lo tienes

def home(request):
    productos = Producto.objects.all()  # Muestra todos los productos del menú
    return render(request, 'inicio/inicio.html', {'productos': productos})
# Create your views here.
