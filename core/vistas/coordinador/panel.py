from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from core.models import Usuario

def es_coordinador(user):
    return user.rol.nombre == 'Coordinador Académico'

@login_required
@user_passes_test(es_coordinador)
def panel_coordinador(request):
    return redirect('usuarios_pendientes')

@login_required
@user_passes_test(es_coordinador)
def usuarios_pendientes(request):
    # Obtener fecha seleccionada desde GET
    fecha = request.GET.get('fecha')

    # Consulta base: usuarios inactivos que NO sean Coordinadores
    usuarios = Usuario.objects.filter(
        is_active=False
    ).exclude(
        rol__nombre__iexact='Coordinador Académico'
    ).select_related('rol')

    # Si se pasó una fecha válida, filtrar
    if fecha:
        try:
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d').date()
            usuarios = usuarios.filter(fecha_registro=fecha_dt)  # Ajusta campo fecha_registro según tu modelo
        except ValueError:
            pass  # Si la fecha es inválida, no aplica filtro

    return render(request, 'panel_coordinador/usuarios_pendientes.html', {
        'pendientes': usuarios,
        'pending_users_count': usuarios.count(),
        'fecha_seleccionada': fecha  # Enviar la fecha al template
    })

@login_required
@user_passes_test(es_coordinador)
def activar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if usuario.rol.nombre == 'Coordinador Académico':
        messages.error(request, "❌ No tienes permisos para activar a otros Coordinadores Académicos. Solo el Superusuario puede hacerlo.")
        return redirect('usuarios_pendientes')

    if usuario.is_active:
        messages.warning(request, f"⚠️ El usuario {usuario.correo} ya está activo.")
    else:
        usuario.is_active = True
        usuario.activado_por = request.user
        usuario.save()
        messages.success(request, f"✅ Usuario {usuario.correo} activado correctamente.")

    return redirect('usuarios_pendientes')

