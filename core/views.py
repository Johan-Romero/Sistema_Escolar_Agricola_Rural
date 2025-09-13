from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    HojaDeVidaDocente,
    EducacionDocente,
    CapacitacionDocente,
    IdiomaDocente,
    ExperienciaDocente
)
from .forms import (
    EducacionDocenteForm,
    CapacitacionDocenteForm,
    IdiomaDocenteForm,
    ExperienciaDocenteForm
)


@login_required
def hoja_de_vida(request):
    """
    Vista principal de la hoja de vida del docente.
    Maneja Educación, Capacitaciones, Idiomas y Experiencia.
    """
    # Crear/obtener hoja de vida del docente
    hoja, created = HojaDeVidaDocente.objects.get_or_create(usuario=request.user)

    if request.method == "POST":
        # Guardar Educación
        if "guardar_educacion" in request.POST:
            form = EducacionDocenteForm(request.POST)
            if form.is_valid():
                educacion = form.save(commit=False)
                educacion.hoja_de_vida = hoja
                educacion.save()
                return redirect("hoja_de_vida")

        # Guardar Capacitación
        elif "guardar_capacitacion" in request.POST:
            form = CapacitacionDocenteForm(request.POST)
            if form.is_valid():
                capacitacion = form.save(commit=False)
                capacitacion.hoja_de_vida = hoja
                capacitacion.save()
                return redirect("hoja_de_vida")

        # Guardar Idioma
        elif "guardar_idioma" in request.POST:
            form = IdiomaDocenteForm(request.POST)
            if form.is_valid():
                idioma = form.save(commit=False)
                idioma.hoja_de_vida = hoja
                idioma.save()
                return redirect("hoja_de_vida")

        # Guardar Experiencia
        elif "guardar_experiencia" in request.POST:
            form = ExperienciaDocenteForm(request.POST)
            if form.is_valid():
                experiencia = form.save(commit=False)
                experiencia.hoja_de_vida = hoja
                experiencia.save()
                return redirect("hoja_de_vida")

    # Contexto con formularios vacíos + registros guardados
    context = {
        "educacion_form": EducacionDocenteForm(),
        "capacitacion_form": CapacitacionDocenteForm(),
        "idioma_form": IdiomaDocenteForm(),
        "experiencia_form": ExperienciaDocenteForm(),
        "educaciones": EducacionDocente.objects.filter(hoja_de_vida=hoja),
        "capacitaciones": CapacitacionDocente.objects.filter(hoja_de_vida=hoja),
        "idiomas": IdiomaDocente.objects.filter(hoja_de_vida=hoja),
        "experiencias": ExperienciaDocente.objects.filter(hoja_de_vida=hoja),
    }

    return render(request, "panel_docente/hoja_de_vida.html", context)
