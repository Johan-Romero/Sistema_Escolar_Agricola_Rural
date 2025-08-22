document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("menu-toggle");
  const menu = document.getElementById("navbar-menu");

  toggleBtn.addEventListener("click", function () {
    menu.classList.toggle("show");
  });
});
