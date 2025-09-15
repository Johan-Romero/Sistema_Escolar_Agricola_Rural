from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from core.models import HojaDeVidaDocente, PerfilDeUsuario
from core.forms import DatosBasicosDocenteForm, IdentificacionForm, IdentidadForm

@login_required

def panel_docente_bienvenida(request):
    return render(request, "panel_docente/bienvenida.html")

def docente_datos_basicos_view(request):
    usuario = request.user

    # Perfil: en memoria si no existe
    perfil = PerfilDeUsuario.objects.filter(usuario=usuario).first()
    if not perfil:
        perfil = PerfilDeUsuario(usuario=usuario)

    # Hoja de vida: en memoria si no existe
    hoja_de_vida = HojaDeVidaDocente.objects.filter(usuario=usuario).first()
    if not hoja_de_vida:
        hoja_de_vida = HojaDeVidaDocente(usuario=usuario)

    # Inicializar datos desde perfil
    initial_basico = {}
    if perfil and hasattr(perfil, "ciudad") and perfil.ciudad:
        initial_basico['direccion_linea1'] = perfil.direccion_linea1
        initial_basico['direccion_linea2'] = perfil.direccion_linea2
        initial_basico['municipio_residencia'] = perfil.ciudad
        if perfil.ciudad and perfil.ciudad.departamento:
            initial_basico['departamento_residencia'] = perfil.ciudad.departamento
            if perfil.ciudad.departamento.pais:
                initial_basico['pais_residencia'] = perfil.ciudad.departamento.pais


    if request.method == 'POST':
        form_identificacion = IdentificacionForm(request.POST, instance=usuario)
        form_identidad = IdentidadForm(request.POST, instance=perfil)
        form_basico = DatosBasicosDocenteForm(request.POST, instance=hoja_de_vida, initial=initial_basico)

        if all([form_identificacion.is_valid(), form_identidad.is_valid(), form_basico.is_valid()]):
            usuario = form_identificacion.save()

            perfil = form_identidad.save(commit=False)
            perfil.usuario = usuario
            perfil.ciudad = form_basico.cleaned_data.get('municipio_residencia')
            perfil.save()

            hoja = form_basico.save(commit=False)
            hoja.usuario = usuario
            hoja.fecha_nacimiento = form_basico.cleaned_data.get('fecha_nacimiento')
            hoja.save()

            messages.success(request, "✅ Información actualizada correctamente.")
            return redirect('panel_docente_bienvenida')
        else:
            messages.error(request, "❌ Corrige los errores en los formularios.")
    else:
        form_identificacion = IdentificacionForm(instance=usuario)
        form_identidad = IdentidadForm(instance=perfil)
        form_basico = DatosBasicosDocenteForm(instance=hoja_de_vida, initial=initial_basico)

    return render(request, 'panel_docente/datos_basicos.html', {
        'form_identificacion': form_identificacion,
        'form_identidad': form_identidad,
        'form_basico': form_basico,
        'hoja': hoja_de_vida,
        'perfil': perfil,
    })
