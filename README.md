# 🏫 Sistema Escolar

Proyecto escolar desarrollado en Django por aprendices del SENA.  
Este sistema permite gestionar currículo, docentes, estudiantes, matrículas y más.

---

## 🚀 Tecnologías utilizadas

- Python 3.10+
- Django 5.x
- Bootstrap
- PostgreSQL 15–17 (en modo desarrollo y producción)venv\Scripts\activate
- Node.js (para compilar Tailwind)

---

## 📦 Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Johan-Romero/Sistema_Escolar_Agricola_Rural.git
cd Sistema_Escolar_Agricula_Rural
pip install -r requirements.txt (Instalar Requerimientos obligatorios)


## Licencia

Copyright © 2025 Juan David Carvajal Montoya

Solo para fines educativos internos en el SENA.  
Se prohíbe la copia, distribución, uso comercial y modificación fuera del contexto de aprendizaje autorizado.

```
SistemaEscolarBootstrap
├─ backend
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ core
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ editar_perfil.html
│  ├─ forms.py
│  ├─ managers.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_eliminar_tablas_huerfanas.py
│  │  ├─ 0003_perfildeusuario_especialidad_perfildeusuario_grupo_and_more.py
│  │  ├─ 0004_perfildeusuario_foto.py
│  │  ├─ 0005_pais_usuario_numero_documento_usuario_tipo_documento_and_more.py
│  │  ├─ 0006_alter_departamento_pais.py
│  │  ├─ 0007_remove_perfildeusuario_numero_documento_and_more.py
│  │  ├─ 0008_estadocivil_estrato_genero_hojadevidadocente_and_more.py
│  │  ├─ 0009_alter_hojadevidadocente_departamento_residencia_and_more.py
│  │  ├─ 0010_perfildeusuario_municipio_identificacion.py
│  │  ├─ 0011_usuario_activado_por.py
│  │  ├─ 0012_alter_usuario_rol.py
│  │  ├─ 0013_remove_perfildeusuario_municipio_identificacion_and_more.py
│  │  ├─ 0014_usuario_activado_por.py
│  │  ├─ 0015_alter_tipodocumento_nombre.py
│  │  ├─ 0016_remove_educaciondocente_hoja_de_vida_and_more.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ perfil_usuario.html
│  ├─ registration
│  │  ├─ password_reset_complete.html
│  │  ├─ password_reset_confirm.html
│  │  ├─ password_reset_done.html
│  │  └─ password_reset_form.html
│  ├─ templates
│  │  ├─ auth_base.html
│  │  ├─ base.html
│  │  ├─ includes
│  │  │  ├─ aside_coordinador.html
│  │  │  ├─ aside_docente.html
│  │  │  ├─ footer.html
│  │  │  └─ navbar.html
│  │  ├─ inicio.html
│  │  ├─ login.html
│  │  ├─ panel_coordinador
│  │  │  ├─ area_form.html
│  │  │  ├─ area_list.html
│  │  │  ├─ asignacion_docente_form.html
│  │  │  ├─ asignacion_docente_list.html
│  │  │  ├─ asignatura_form.html
│  │  │  ├─ asignatura_list.html
│  │  │  ├─ aula_form.html
│  │  │  ├─ aula_list.html
│  │  │  ├─ dashboard_base.html
│  │  │  ├─ grado_form.html
│  │  │  ├─ grado_list.html
│  │  │  ├─ grupo_form.html
│  │  │  ├─ grupo_list.html
│  │  │  ├─ nivel_form.html
│  │  │  ├─ nivel_list.html
│  │  │  ├─ panel.html
│  │  │  ├─ panel_1.html
│  │  │  ├─ panel_base.html
│  │  │  ├─ panel_coordinador.html
│  │  │  └─ usuarios_pendientes.html
│  │  ├─ panel_docente
│  │  │  ├─ capacitacion.html
│  │  │  ├─ dashboard_base.html
│  │  │  ├─ datos_basicos.html
│  │  │  ├─ educacion.html
│  │  │  ├─ experiencia.html
│  │  │  ├─ idiomas.html
│  │  │  └─ panel_docente.html
│  │  └─ registro.html
│  ├─ templates.zip
│  ├─ templatetags
│  │  ├─ custom_tags.py
│  │  ├─ form_extras.py
│  │  └─ __init__.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ vistas
│  │  ├─ acudiente
│  │  │  ├─ panel.py
│  │  │  └─ __init__.py
│  │  ├─ ajax
│  │  │  └─ ubicaciones.py
│  │  ├─ autenticacion
│  │  │  ├─ autenticacion.py
│  │  │  └─ __init__.py
│  │  ├─ coordinador
│  │  │  ├─ gestion_academica.py
│  │  │  ├─ panel.py
│  │  │  └─ __init__.py
│  │  ├─ docente
│  │  │  ├─ capacitacion.py
│  │  │  ├─ docente_hoja_vida.py
│  │  │  ├─ educacion.py
│  │  │  ├─ experiencia.py
│  │  │  ├─ idiomas.py
│  │  │  ├─ panel.py
│  │  │  └─ __init__.py
│  │  ├─ estudiante
│  │  │  ├─ panel.py
│  │  │  └─ __init__.py
│  │  ├─ navegacion
│  │  │  ├─ inicio.py
│  │  │  └─ __init__.py
│  │  ├─ perfil
│  │  │  ├─ perfil_usuario.py
│  │  │  └─ __init__.py
│  │  ├─ utilidades
│  │  │  ├─ permisos.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ vistas.zip
│  └─ __init__.py
├─ LICENSE
├─ manage.py
├─ package-lock.json
├─ package.json
├─ postcss.config.js
├─ README.md
├─ requirements.txt
├─ staticfiles
│  ├─ admin
│  │  ├─ css
│  │  │  ├─ autocomplete.css
│  │  │  ├─ base.css
│  │  │  ├─ changelists.css
│  │  │  ├─ dark_mode.css
│  │  │  ├─ dashboard.css
│  │  │  ├─ forms.css
│  │  │  ├─ login.css
│  │  │  ├─ nav_sidebar.css
│  │  │  ├─ responsive.css
│  │  │  ├─ responsive_rtl.css
│  │  │  ├─ rtl.css
│  │  │  ├─ unusable_password_field.css
│  │  │  ├─ vendor
│  │  │  │  └─ select2
│  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │     ├─ select2.css
│  │  │  │     └─ select2.min.css
│  │  │  └─ widgets.css
│  │  ├─ img
│  │  │  ├─ calendar-icons.svg
│  │  │  ├─ gis
│  │  │  │  ├─ move_vertex_off.svg
│  │  │  │  └─ move_vertex_on.svg
│  │  │  ├─ icon-addlink.svg
│  │  │  ├─ icon-alert.svg
│  │  │  ├─ icon-calendar.svg
│  │  │  ├─ icon-changelink.svg
│  │  │  ├─ icon-clock.svg
│  │  │  ├─ icon-deletelink.svg
│  │  │  ├─ icon-hidelink.svg
│  │  │  ├─ icon-no.svg
│  │  │  ├─ icon-unknown-alt.svg
│  │  │  ├─ icon-unknown.svg
│  │  │  ├─ icon-viewlink.svg
│  │  │  ├─ icon-yes.svg
│  │  │  ├─ inline-delete.svg
│  │  │  ├─ LICENSE
│  │  │  ├─ README.txt
│  │  │  ├─ search.svg
│  │  │  ├─ selector-icons.svg
│  │  │  ├─ sorting-icons.svg
│  │  │  ├─ tooltag-add.svg
│  │  │  └─ tooltag-arrowright.svg
│  │  └─ js
│  │     ├─ actions.js
│  │     ├─ admin
│  │     │  ├─ DateTimeShortcuts.js
│  │     │  └─ RelatedObjectLookups.js
│  │     ├─ autocomplete.js
│  │     ├─ calendar.js
│  │     ├─ cancel.js
│  │     ├─ change_form.js
│  │     ├─ core.js
│  │     ├─ filters.js
│  │     ├─ inlines.js
│  │     ├─ jquery.init.js
│  │     ├─ nav_sidebar.js
│  │     ├─ popup_response.js
│  │     ├─ prepopulate.js
│  │     ├─ prepopulate_init.js
│  │     ├─ SelectBox.js
│  │     ├─ SelectFilter2.js
│  │     ├─ theme.js
│  │     ├─ unusable_password_field.js
│  │     ├─ urlify.js
│  │     └─ vendor
│  │        ├─ jquery
│  │        │  ├─ jquery.js
│  │        │  ├─ jquery.min.js
│  │        │  └─ LICENSE.txt
│  │        ├─ select2
│  │        │  ├─ i18n
│  │        │  │  ├─ af.js
│  │        │  │  ├─ ar.js
│  │        │  │  ├─ az.js
│  │        │  │  ├─ bg.js
│  │        │  │  ├─ bn.js
│  │        │  │  ├─ bs.js
│  │        │  │  ├─ ca.js
│  │        │  │  ├─ cs.js
│  │        │  │  ├─ da.js
│  │        │  │  ├─ de.js
│  │        │  │  ├─ dsb.js
│  │        │  │  ├─ el.js
│  │        │  │  ├─ en.js
│  │        │  │  ├─ es.js
│  │        │  │  ├─ et.js
│  │        │  │  ├─ eu.js
│  │        │  │  ├─ fa.js
│  │        │  │  ├─ fi.js
│  │        │  │  ├─ fr.js
│  │        │  │  ├─ gl.js
│  │        │  │  ├─ he.js
│  │        │  │  ├─ hi.js
│  │        │  │  ├─ hr.js
│  │        │  │  ├─ hsb.js
│  │        │  │  ├─ hu.js
│  │        │  │  ├─ hy.js
│  │        │  │  ├─ id.js
│  │        │  │  ├─ is.js
│  │        │  │  ├─ it.js
│  │        │  │  ├─ ja.js
│  │        │  │  ├─ ka.js
│  │        │  │  ├─ km.js
│  │        │  │  ├─ ko.js
│  │        │  │  ├─ lt.js
│  │        │  │  ├─ lv.js
│  │        │  │  ├─ mk.js
│  │        │  │  ├─ ms.js
│  │        │  │  ├─ nb.js
│  │        │  │  ├─ ne.js
│  │        │  │  ├─ nl.js
│  │        │  │  ├─ pl.js
│  │        │  │  ├─ ps.js
│  │        │  │  ├─ pt-BR.js
│  │        │  │  ├─ pt.js
│  │        │  │  ├─ ro.js
│  │        │  │  ├─ ru.js
│  │        │  │  ├─ sk.js
│  │        │  │  ├─ sl.js
│  │        │  │  ├─ sq.js
│  │        │  │  ├─ sr-Cyrl.js
│  │        │  │  ├─ sr.js
│  │        │  │  ├─ sv.js
│  │        │  │  ├─ th.js
│  │        │  │  ├─ tk.js
│  │        │  │  ├─ tr.js
│  │        │  │  ├─ uk.js
│  │        │  │  ├─ vi.js
│  │        │  │  ├─ zh-CN.js
│  │        │  │  └─ zh-TW.js
│  │        │  ├─ LICENSE.md
│  │        │  ├─ select2.full.js
│  │        │  └─ select2.full.min.js
│  │        └─ xregexp
│  │           ├─ LICENSE.txt
│  │           ├─ xregexp.js
│  │           └─ xregexp.min.js
│  ├─ css
│  │  ├─ input.css
│  │  └─ tailwind.css
│  ├─ debug_toolbar
│  │  ├─ css
│  │  │  ├─ print.css
│  │  │  └─ toolbar.css
│  │  └─ js
│  │     ├─ history.js
│  │     ├─ redirect.js
│  │     ├─ timer.js
│  │     ├─ toolbar.js
│  │     └─ utils.js
│  └─ img
│     ├─ asignatura.png
│     ├─ book-themes_32_32.png
│     ├─ classroom.png
│     ├─ classroom_32_32.png
│     ├─ close_32_32.png
│     ├─ curriculum-management.png
│     ├─ default_avatar.png
│     ├─ education-grade.png
│     ├─ education-group.png
│     ├─ education-level.png
│     ├─ education-levels_32_32.png
│     ├─ education-medal.png
│     ├─ education-medal_32_32.png
│     ├─ education_subject.png
│     ├─ enrollment.png
│     ├─ experience-transfer_32_32.png
│     ├─ facilities.png
│     ├─ grade-level_32_32.png
│     ├─ identity-verification_32_32.png
│     ├─ instructor-group_32_32.png
│     ├─ instructor-lecture.png
│     ├─ knowledge-area.png
│     ├─ knowledge-areas_32_32.png
│     └─ student-group_32_32.png
└─ tailwind.config.js

```