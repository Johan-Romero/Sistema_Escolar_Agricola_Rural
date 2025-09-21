import re
from django.contrib.auth import authenticate
from django import forms
from django.forms import TextInput, Select, EmailInput, FileInput, PasswordInput
# from django.contrib.auth.hashers import make_password

from .models import (
    Usuario, Rol, TipoDocumento, Ciudad, Pais, Departamento,
    NivelEducativo, Grado, Area, Asignatura, Tema, Logro,
    Aula, Grupo, AsignacionDocente,
    PerfilDeUsuario,
    HojaDeVidaDocente, EducacionDocente, CapacitacionDocente,
    IdiomaDocente, ExperienciaDocente, EducacionDocente
)





# Formulario de Registro de Usuario
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={'class': 'w-full p-2 border rounded'}),
        help_text="Debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un símbolo (#$%!)."
    )
    confirmar_password = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirmar contraseña",
            "required": "required"  # 👈 agregado
        })
    )

    # Campos auxiliares para ubicación de expedición
    pais_identificacion = forms.ModelChoiceField(
        label="País de expedición",
        queryset=Pais.objects.all(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )
    departamento_identificacion = forms.ModelChoiceField(
        label="Departamento de expedición",
        queryset=Departamento.objects.none(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )
    municipio_identificacion = forms.ModelChoiceField(
        label="Municipio de expedición",
        queryset=Ciudad.objects.none(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = Usuario
        fields = ["correo", "rol", "tipo_documento", "numero_documento",
                  "pais_identificacion", "departamento_identificacion",
                  "municipio_identificacion", "password"]

        widgets = {
            "correo": forms.EmailInput(attrs={"class": "form-control", "required": True}),
            "rol": forms.Select(attrs={"class": "form-select", "required": True}),
            "tipo_documento": forms.Select(attrs={"class": "form-select", "required": True}),
            "numero_documento": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "pais_identificacion": forms.Select(attrs={"class": "form-select", "required": True}),
            "departamento_identificacion": forms.Select(attrs={"class": "form-select", "required": True}),
            "municipio_identificacion": forms.Select(attrs={"class": "form-select", "required": True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "required": True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ordenar roles por ID
        self.fields['rol'].queryset = Rol.objects.all().order_by('id')

        # Cargar departamentos si hay país en los datos
        if 'pais_identificacion' in self.data:
            try:
                pais_id = int(self.data.get('pais_identificacion'))
                self.fields['departamento_identificacion'].queryset = Departamento.objects.filter(pais_id=pais_id)
            except (ValueError, TypeError):
                self.fields['departamento_identificacion'].queryset = Departamento.objects.none()

        # Cargar ciudades si hay departamento en los datos
        if 'departamento_identificacion' in self.data:
            try:
                departamento_id = int(self.data.get('departamento_identificacion'))
                self.fields['municipio_identificacion'].queryset = Ciudad.objects.filter(departamento_id=departamento_id)
            except (ValueError, TypeError):
                self.fields['municipio_identificacion'].queryset = Ciudad.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")

        if password and confirmar:
            if password != confirmar:
                self.add_error("confirmar_password", "⚠️ Las contraseñas no coinciden.")
            if len(password) < 8:
                self.add_error("password", "🔒 La contraseña debe tener al menos 8 caracteres.")
            if not re.search(r'[A-Z]', password):
                self.add_error("password", "🔒 Debe incluir al menos una letra mayúscula.")
            if not re.search(r'[a-z]', password):
                self.add_error("password", "🔒 Debe incluir al menos una letra minúscula.")
            if not re.search(r'\d', password):
                self.add_error("password", "🔒 Debe incluir al menos un número.")
            if not re.search(r'[#\$%!_]', password):
                self.add_error("password", "🔒 Debe incluir al menos un símbolo especial: # $ % ! _")

        return cleaned_data


    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        usuario.municipio_identificacion = self.cleaned_data.get("municipio_identificacion")
        usuario.is_active = False
        usuario.is_superuser = False
        usuario.is_staff = False

        if commit:
            usuario.save()

        return usuario


    
# Formulario para Perfil de Usuario
class PerfilUsuarioForm(forms.ModelForm):
    correo = forms.EmailField(label="Correo electrónico", required=True, disabled=True)

    tipo_documento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.all(),
        required=False,
        label="Tipo de Documento"
    )
    numero_documento = forms.CharField(
        required=False,
        label="Número de Documento"
    )
    municipio_identificacion = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=False,
        label="Municipio de expedición"
    )
    ciudad = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=True,
        label="Ciudad de residencia",
        error_messages={
            'required': "La ciudad de residencia es obligatoria."
        }
    )

    class Meta:
        model = PerfilDeUsuario
        fields = [
            'foto',
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'direccion_linea1', 'direccion_linea2', 'ciudad',
            'especialidad', 'grupo', 'acudidos'
        ]
        widgets = {
            'foto': FileInput(),
            'primer_nombre': TextInput(),
            'segundo_nombre': TextInput(),
            'primer_apellido': TextInput(),
            'segundo_apellido': TextInput(),
            'direccion_linea1': TextInput(),
            'direccion_linea2': TextInput(),
            'ciudad': Select(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Inicializa datos desde usuario autenticado si existen
        if self.user:
            self.fields['correo'].initial = self.user.correo
            self.fields['tipo_documento'].initial = self.user.tipo_documento
            self.fields['numero_documento'].initial = self.user.numero_documento
            self.fields['municipio_identificacion'].initial = self.user.municipio_identificacion

        # Campos que se muestran según rol
        campos_visibles = [
            'foto', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'tipo_documento', 'numero_documento', 'municipio_identificacion',
            'direccion_linea1', 'direccion_linea2', 'ciudad'
        ]

        if self.user and self.user.rol:
            rol = self.user.rol.nombre.strip().lower()
            if rol == 'docente':
                campos_visibles.append('especialidad')
                self.fields['especialidad'].required = True
            elif rol == 'estudiante':
                campos_visibles.append('grupo')
                self.fields['grupo'].required = True
            elif rol in ['acudiente', 'padre de familia o acudiente']:
                campos_visibles.append('acudidos')
                self.fields['acudidos'].queryset = PerfilDeUsuario.objects.filter(
                    usuario__rol__nombre__iexact='estudiante'
                )
                self.fields['acudidos'].required = False

        for field in list(self.fields):
            if field not in campos_visibles and field != 'correo':
                del self.fields[field]

    def clean_ciudad(self):
        ciudad = self.cleaned_data.get('ciudad')
        if not ciudad:
            raise forms.ValidationError("La ciudad de residencia es obligatoria.")
        return ciudad

    def save(self, commit=True):
        perfil = super().save(commit=False)

        # Actualiza los datos básicos en usuario también
        if self.user:
            self.user.tipo_documento = self.cleaned_data.get('tipo_documento')
            self.user.numero_documento = self.cleaned_data.get('numero_documento')
            self.user.municipio_identificacion = self.cleaned_data.get('municipio_identificacion')
            if commit:
                self.user.save()

        if commit:
            perfil.save()
            self.save_m2m()

        return perfil





class LoginForm(forms.Form):
    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )

# Formulario para Nivel Educativo
class NivelEducativoForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['nombre']

# Formulario para Grado
class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nivel', 'nombre']
        
# Formulario para Aula
class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
            'estado': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
        }



# Formulario para Grupo
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'grado', 'aula']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        grado = cleaned_data.get('grado')
        if Grupo.objects.filter(nombre=nombre, grado=grado).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un grupo con ese nombre en el mismo grado.")
        return cleaned_data


# Formulario para Asignación de Docente
class AsignacionDocenteForm(forms.ModelForm):
    class Meta:
        model = AsignacionDocente
        fields = ['docente', 'asignatura', 'grupo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo usuarios con rol "Docente"
        self.fields['docente'].queryset = Usuario.objects.filter(rol__nombre__iexact='Docente')


# Formulario para Área
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'obligatoria']

# Formulario para Asignatura
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'grado', 'area']

# Formulario para Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nombre', 'asignatura']

# Formulario para Logro
class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['descripcion', 'asignatura']

# Hoja de Vida Docentes
class DatosBasicosDocenteForm(forms.ModelForm):
    municipio_residencia = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=True,
        label="Ciudad de Residencia",
        error_messages={'required': "La ciudad de residencia es obligatoria."}
    )
    
    class Meta:
        model = HojaDeVidaDocente
        exclude = ['usuario']  # Usuario se asigna en la vista

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'genero': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'estado_civil': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'pais_residencia': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'departamento_residencia': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'municipio_residencia': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'direccion_linea1': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'direccion_linea2': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'estrato': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'telefono_celular': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'telefono_celular_alterno': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'telefono_fijo': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'telefono_fijo_ext': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'correo_alterno': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'resumen': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
        }

# Identificación Formulario
class IdentificacionForm(forms.ModelForm):
    municipio_identificacion = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        label="Municipio de Identificación",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full border border-gray-300 rounded px-3 py-2'
        })
    )

    class Meta:
        model = Usuario
        fields = ['tipo_documento', 'numero_documento', 'municipio_identificacion']  # 👈 AGRÉGALO AQUÍ
        widgets = {
            'tipo_documento': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            # Puedes personalizar municipio_identificacion aquí si prefieres
        }


        
# Identidad Form
class IdentidadForm(forms.ModelForm):
    class Meta:
        model = PerfilDeUsuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2'
            }),
        }

from django import forms
from .models import EducacionDocente   # 👈 importa tu modelo (ajusta el nombre real del modelo)

class EducacionDocenteForm(forms.ModelForm):
    class Meta:
        model = EducacionDocente   # 👈 asegúrate de que este es el nombre de tu modelo
        fields = ['nivel', 'institucion', 'titulo_obtenido', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'nivel': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_obtenido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class CapacitacionDocenteForm(forms.ModelForm):
    class Meta:
        model = CapacitacionDocente
        fields = '__all__'

class IdiomaDocenteForm(forms.ModelForm):
    class Meta:
        model = IdiomaDocente
        fields = '__all__'

class ExperienciaDocenteForm(forms.ModelForm):
    class Meta:
        model = ExperienciaDocente
        fields = '__all__' 

# Formulario de Contacto
class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Tu Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    correo = forms.EmailField(
        label="Tu Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    asunto = forms.CharField(
        label="Asunto",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
