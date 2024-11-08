from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pedido  # Asume que tienes un modelo Pedido

@login_required
def nuevo_pedido(request):
    if request.method == 'POST':
        # Procesa el pedido aquí (esto es solo un ejemplo)
        pedido = Pedido.objects.create(usuario=request.user, estado='Pendiente')
        return redirect('historial_pedidos')
    return render(request, 'pedidos/nuevo_pedido.html')

@login_required
def historial_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos/historial_pedidos.html', {'pedidos': pedidos})
# Create your views here.
