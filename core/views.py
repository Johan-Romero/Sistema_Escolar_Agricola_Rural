from django.shortcuts import render, redirect
from .models import EducacionDocente
from .forms import EducacionDocenteForm
from django.contrib.auth.decorators import login_required

@login_required
def educacion_docente(request):
    if request.method == "POST":
        form = EducacionDocenteForm(request.POST)
        if form.is_valid():
            educacion = form.save(commit=False)
            educacion.docente = request.user  # asigna el usuario logueado
            educacion.save()
            return redirect("educacion_docente")  # redirige a la misma página
    else:
        form = EducacionDocenteForm()

    # obtener las educaciones registradas del docente
    educaciones = EducacionDocente.objects.filter(docente=request.user)

    return render(request, "panel_docente/educacion.html", {
        "form": form,
        "educaciones": educaciones
    })