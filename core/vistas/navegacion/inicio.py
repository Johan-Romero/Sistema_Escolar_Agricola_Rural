from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import ContactoForm
from django.core.mail import send_mail

def bienvenida(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            try:
                send_mail(
                    f'Contacto: {asunto}',
                    f'De: {nombre} <{correo}>\\n\\n{mensaje}',
                    'noreply@agricolarural.edu.co',
                    ['admin@agricolarural.edu.co'],
                    fail_silently=False,
                )
                messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            except Exception as e:
                messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, inténtalo de nuevo más tarde.')

            return redirect('bienvenida')
    else:
        form = ContactoForm()

    return render(request, 'inicio.html', {'form': form})


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
