from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm  # Asume que tienes un formulario para editar el perfil

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
# Create your views here.
