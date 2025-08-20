// static/js/scroll.js
document.addEventListener("DOMContentLoaded", function() {
    // 🔹 Forzar que al cargar la página comience arriba
    if (history.scrollRestoration) {
        history.scrollRestoration = "manual"; 
    }
    window.scrollTo(0, 0);

    // 🔹 Agregar scroll suave solo cuando se hace click en un enlace con #
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });
});
