from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Cuenta creada con éxito.')
            return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'log/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'log/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
# Create your views here.
