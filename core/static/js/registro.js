// 👁️ Mostrar / ocultar contraseña
function togglePasswordIcon(id, btn) {
    const field = document.getElementById(id);
    if (!field) return;
    const icon = btn.querySelector("i");
    if (field.type === "password") {
        field.type = "text";
        icon.classList.replace("bi-eye-slash", "bi-eye");
    } else {
        field.type = "password";
        icon.classList.replace("bi-eye", "bi-eye-slash");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ registro.js cargado correctamente");

    // ================================
    // Barra de progreso de contraseña
    // ================================
    const passwordField = document.getElementById("id_password");
    const bar = document.getElementById("password-strength");
    const checks = {
        len: document.getElementById("len"),
        mayus: document.getElementById("mayus"),
        minus: document.getElementById("minus"),
        num: document.getElementById("num"),
        sym: document.getElementById("sym"),
    };

    if (passwordField && bar) {
        passwordField.addEventListener("input", function () {
            const value = passwordField.value;
            let score = 0;

            if (value.length >= 8) { 
                score++; 
                checks.len.classList.add("valid"); 
            } else { 
                checks.len.classList.remove("valid"); 
            }

            if (/[A-Z]/.test(value)) { 
                score++; 
                checks.mayus.classList.add("valid"); 
            } else { 
                checks.mayus.classList.remove("valid"); 
            }

            if (/[a-z]/.test(value)) { 
                score++; 
                checks.minus.classList.add("valid"); 
            } else { 
                checks.minus.classList.remove("valid"); 
            }

            if (/\d/.test(value)) { 
                score++; 
                checks.num.classList.add("valid"); 
            } else { 
                checks.num.classList.remove("valid"); 
            }

            if (/[#\$%!_]/.test(value)) { 
                score++; 
                checks.sym.classList.add("valid"); 
            } else { 
                checks.sym.classList.remove("valid"); 
            }

            const percentage = (score / 5) * 100;
            bar.style.width = percentage + "%";
            bar.className = "progress-bar";
            if (percentage < 40) bar.classList.add("bg-danger");
            else if (percentage < 80) bar.classList.add("bg-warning");
            else bar.classList.add("bg-success");
        });
    }

    // ================================
    // País → Departamento → Municipio
    // ================================
    const paisSelect = document.getElementById("id_pais_identificacion");
    const departamentoSelect = document.getElementById("id_departamento_identificacion");
    const municipioSelect = document.getElementById("id_municipio_identificacion");

    if (paisSelect && departamentoSelect && municipioSelect) {
        paisSelect.addEventListener("change", function () {
            const paisId = this.value;
            departamentoSelect.innerHTML = '<option value="">Cargando...</option>';
            municipioSelect.innerHTML = '<option value="">Seleccione municipio</option>';
            if (!paisId) return;
            fetch(`/ajax/departamentos/?pais_id=${paisId}`)
                .then(res => res.json())
                .then(data => {
                    departamentoSelect.innerHTML = '<option value="">Seleccione un departamento</option>';
                    data.forEach(dep => {
                        departamentoSelect.innerHTML += `<option value="${dep.id}">${dep.nombre}</option>`;
                    });
                });
        });

        departamentoSelect.addEventListener("change", function () {
            const depId = this.value;
            municipioSelect.innerHTML = '<option value="">Cargando...</option>';
            if (!depId) return;
            fetch(`/ajax/ciudades/?departamento_id=${depId}`)
                .then(res => res.json())
                .then(data => {
                    municipioSelect.innerHTML = '<option value="">Seleccione municipio</option>';
                    data.forEach(mun => {
                        municipioSelect.innerHTML += `<option value="${mun.id}">${mun.nombre}</option>`;
                    });
                });
        });
    }

    // ================================
    // Alerta para Coordinador
    // ================================
    const rolSelect = document.getElementById("id_rol");
    const alertaDiv = document.getElementById("coordinador-alerta");
    if (rolSelect && alertaDiv) {
        const toggleAlerta = () => {
            const selectedText = rolSelect.options[rolSelect.selectedIndex]?.text.toLowerCase();
            if (selectedText.includes("coordinador")) {
                alertaDiv.classList.remove("d-none");
            } else {
                alertaDiv.classList.add("d-none");
            }
        };
        rolSelect.addEventListener("change", toggleAlerta);
        toggleAlerta();
    }

    // ================================
    // Cambiar entre modales
    // ================================
    document.querySelectorAll(".modal-switcher").forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const target = this.getAttribute("data-bs-target");
            const currentModal = bootstrap.Modal.getInstance(this.closest(".modal"));
            if (currentModal) currentModal.hide();
            const newModal = new bootstrap.Modal(document.querySelector(target));
            newModal.show();
        });
    });
});

