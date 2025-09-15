console.log("✅ scroll.js y right_panel.js cargados correctamente");

document.addEventListener("DOMContentLoaded", function () {
  /* ===============================
     SCROLL: activar link según sección
     =============================== */
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".school-nav .nav-link");

  function activarLink() {
    let scrollY = window.scrollY;
    let foundSection = false;

    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 130;
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

    if (!foundSection && scrollY < 200) {
      navLinks.forEach((link) => link.classList.remove("active"));
    }
  }

  window.addEventListener("scroll", activarLink);
  activarLink();

  /* ===============================
     SIDEBAR: botones activos
     =============================== */
  const sidebarLinks = document.querySelectorAll(".dashboard-sidebar .menu-link");

  sidebarLinks.forEach(link => {
    link.addEventListener("click", function () {
      sidebarLinks.forEach(l => l.classList.remove("active"));
      this.classList.add("active");
    });
  });

  // Mantener activo según URL
  const currentPath = window.location.pathname;
  sidebarLinks.forEach(link => {
    if(link.getAttribute("href") === currentPath){
      link.classList.add("active");
    }
  });

  /* ===============================
     RIGHT PANEL: notas rápidas
     =============================== */
  console.log("right_panel.js cargado");

  // Inicializar dropdowns (Bootstrap)
  try {
    if (typeof bootstrap !== "undefined" && bootstrap.Dropdown) {
      document.querySelectorAll('[data-bs-toggle="dropdown"]').forEach(btn => {
        if (!bootstrap.Dropdown.getInstance(btn)) {
          new bootstrap.Dropdown(btn);
        }
      });
    }
  } catch (e) {
    console.warn("Error inicializando dropdowns:", e);
  }

  // Variables de notas
  const noteTitleEl = document.getElementById("noteTitle");
  const notesArea = document.getElementById("notes");
  const saveBtn = document.getElementById("saveNotes");
  const notesList = document.getElementById("notesList");

  const noteModalEl = document.getElementById("noteModal");
  const noteModalTitle = document.getElementById("noteModalTitle");
  const noteModalDate = document.getElementById("noteModalDate");
  const noteModalContent = document.getElementById("noteModalContent");
  const deleteNoteBtn = document.getElementById("deleteNoteBtn");
  let modalInstance = null;
  if (noteModalEl && typeof bootstrap !== "undefined" && bootstrap.Modal) {
    modalInstance = new bootstrap.Modal(noteModalEl);
  }

  if (!notesArea || !saveBtn || !notesList) {
    console.warn("Elementos de notas no encontrados en el DOM. Abortando lógica de notas.");
    return;
  }

  // cargar notas
  let notes = [];
  try {
    const raw = localStorage.getItem("docente_notes");
    if (raw) {
      const parsed = JSON.parse(raw);
      if (Array.isArray(parsed)) notes = parsed;
    }
  } catch (e) {
    console.warn("LocalStorage corrupto: limpiando docente_notes", e);
    localStorage.removeItem("docente_notes");
    notes = [];
  }

  function saveNotesToStorage() {
    localStorage.setItem("docente_notes", JSON.stringify(notes));
  }

  function renderNotes() {
    notesList.innerHTML = "";
    if (!notes.length) {
      const li = document.createElement("li");
      li.className = "list-group-item text-muted";
      li.textContent = "No hay notas guardadas";
      notesList.appendChild(li);
      return;
    }

    const notesCopy = notes.slice().reverse();
    notesCopy.forEach(note => {
      const li = document.createElement("li");
      li.className = "list-group-item d-flex justify-content-between align-items-center";
      li.dataset.noteId = note.id;

      const left = document.createElement("div");
      left.style.flex = "1 1 auto";
      left.style.minWidth = "0";
      left.style.cursor = "pointer";

      const title = document.createElement("div");
      title.className = "note-title fw-semibold";
      title.textContent = note.title || "Sin título";
      title.style.whiteSpace = "nowrap";
      title.style.overflow = "hidden";
      title.style.textOverflow = "ellipsis";

      const meta = document.createElement("div");
      meta.className = "note-meta text-muted small";
      meta.textContent = note.date || "";

      left.appendChild(title);
      left.appendChild(meta);

      left.addEventListener("click", function () {
        if (noteModalTitle) noteModalTitle.textContent = note.title || "Sin título";
        if (noteModalDate) noteModalDate.textContent = note.date || "";
        if (noteModalContent) noteModalContent.textContent = note.content || "";
        if (deleteNoteBtn) deleteNoteBtn.dataset.noteId = note.id;
        if (modalInstance) modalInstance.show();
      });

      const actions = document.createElement("div");
      actions.className = "note-actions d-flex flex-column gap-1";

      const viewBtn = document.createElement("button");
      viewBtn.className = "btn btn-sm btn-outline-primary";
      viewBtn.type = "button";
      viewBtn.textContent = "Ver";
      viewBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        if (noteModalTitle) noteModalTitle.textContent = note.title || "Sin título";
        if (noteModalDate) noteModalDate.textContent = note.date || "";
        if (noteModalContent) noteModalContent.textContent = note.content || "";
        if (deleteNoteBtn) deleteNoteBtn.dataset.noteId = note.id;
        if (modalInstance) modalInstance.show();
      });

      const delBtn = document.createElement("button");
      delBtn.className = "btn btn-sm btn-danger";
      delBtn.type = "button";
      delBtn.innerHTML = '<i class="bi bi-trash"></i>';
      delBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        notes = notes.filter(n => n.id !== note.id);
        saveNotesToStorage();
        renderNotes();
      });

      actions.appendChild(viewBtn);
      actions.appendChild(delBtn);

      li.appendChild(left);
      li.appendChild(actions);
      notesList.appendChild(li);
    });

    notesList.scrollTop = 0;
  }

  saveBtn.addEventListener("click", function () {
    const title = (noteTitleEl && noteTitleEl.value) ? noteTitleEl.value.trim() : "";
    const content = notesArea.value.trim();
    if (!content) {
      alert("Escribe algo antes de guardar.");
      return;
    }
    const noteObj = {
      id: Date.now().toString(),
      title: title || "Sin título",
      content: content,
      date: new Date().toLocaleString()
    };
    notes.push(noteObj);
    saveNotesToStorage();
    if (noteTitleEl) noteTitleEl.value = "";
    notesArea.value = "";
    renderNotes();
  });

  if (deleteNoteBtn) {
    deleteNoteBtn.addEventListener("click", function () {
      const id = this.dataset.noteId;
      if (!id) return;
      notes = notes.filter(n => n.id !== id);
      saveNotesToStorage();
      renderNotes();
      if (modalInstance) modalInstance.hide();
    });
  }

  // render inicial
  renderNotes();
});
