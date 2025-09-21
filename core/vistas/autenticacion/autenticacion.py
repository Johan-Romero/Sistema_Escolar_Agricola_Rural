from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from core.forms import RegistroUsuarioForm, PerfilUsuarioForm, LoginForm, ContactoForm
from core.models import PerfilDeUsuario, Rol, Usuario


def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data["correo"]
            password = form.cleaned_data["password"]

            try:
                usuario = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                messages.error(request, "❌ Usuario o contraseña incorrectos.")
                return redirect("/bienvenida/?login=error")

            if not usuario.is_active:
                if usuario.rol and usuario.rol.nombre.lower() == "coordinador académico":
                    messages.error(request, "🕒 Tu cuenta como Coordinador Académico aún no ha sido activada por el superusuario.")
                else:
                    messages.error(request, "🕒 Tu cuenta aún no ha sido activada. Espera la validación.")
                return redirect("/bienvenida/?login=error")

            usuario_autenticado = authenticate(correo=correo, password=password)
            if usuario_autenticado is None:
                messages.error(request, "❌ Usuario o contraseña incorrectos.")
                return redirect("/bienvenida/?login=error")

            login(request, usuario_autenticado)

            # Redirección según el rol
            nombre_rol = usuario.rol.nombre.lower()
            if nombre_rol == "coordinador académico":
                return redirect('panel_coordinador')
            elif nombre_rol == "docente":
                return redirect('panel_docente')
            elif nombre_rol == "estudiante":
                return redirect('panel_estudiante')
            elif nombre_rol in ["acudiente", "padre de familia o acudiente"]:
                return redirect('panel_acudiente')
            else:
                return redirect('inicio')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def logout_usuario(request):
    logout(request)
    return redirect('bienvenida')


def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.white(request, "✅ Registro exitoso. Tu cuenta será activada por un administrador.")
            # Redirige a bienvenida pero abre login modal
            return redirect("/bienvenida/?login=1")
    else:
        form = RegistroUsuarioForm()
    return render(request, "inicio.html", {
        "registro_modal_form": form,
        "login_modal_form": LoginForm()
    })