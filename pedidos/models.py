from django.db import models
from usuarios.models import Usuario
from menu.models import Producto

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En Preparación'),
        ('entregado', 'Entregado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

# Create your models here.
