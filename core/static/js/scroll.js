document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".school-nav .nav-link");

  function activarLink() {
    let scrollY = window.scrollY;

    let foundSection = false; // 👈 para saber si alguna sección fue encontrada

    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 130; // margen para navbar
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute("id");

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === "#" + sectionId) {
            link.classList.add("active");
          }
        });
        foundSection = true;
      }
    });

    // 👇 Si estoy arriba de todo, desmarcar todo
    if (!foundSection && scrollY < 200) {
      navLinks.forEach((link) => link.classList.remove("active"));
    }
  }

  window.addEventListener("scroll", activarLink);
  activarLink(); // correrlo al inicio
});
