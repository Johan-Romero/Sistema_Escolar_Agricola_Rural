from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import ContactoForm
from django.core.mail import send_mail

from core.forms import ContactoForm, RegistroUsuarioForm, LoginForm

def bienvenida(request):
    login_modal_form = LoginForm()
    registro_modal_form = RegistroUsuarioForm()

    if request.method == "POST":
        if "registro" in request.POST:
            registro_modal_form = RegistroUsuarioForm(request.POST)
            if registro_modal_form.is_valid():
                registro_modal_form.save()
                messages.success(request, "✅ Registro exitoso. Tu cuenta será activada por un administrador.")
                return redirect("bienvenida")
        elif "login" in request.POST:
            login_modal_form = LoginForm(request.POST)
            if login_modal_form.is_valid():
                usuario = login_modal_form.cleaned_data["usuario"]
                login(request, usuario)
                return redirect("bienvenida")

    return render(request, "inicio.html", {
        "login_modal_form": login_modal_form,
        "registro_modal_form": registro_modal_form,
    })



@login_required
def inicio(request):
    user = request.user

    if user.is_superuser:
        return redirect('/admin/')

    if user.rol is None:
        messages.error(request, "Tu cuenta no tiene un rol asignado. Contacta al administrador.")
        return redirect('logout')

    rol = user.rol.nombre
    redirecciones = {
        'Coordinador Académico': 'panel_coordinador',
        'Docente': 'panel_docente',
        'Estudiante': 'panel_estudiante',
        'Acudiente': 'panel_acudiente',
        'Padre de Familia o Acudiente': 'panel_acudiente',
    }

    return redirect(redirecciones.get(rol, 'login'))
