// static/js/modal.js
document.addEventListener('DOMContentLoaded', function () {

  // -------- helpers ----------
  function cleanBackdropsAndBody() {
    document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
    document.body.classList.remove('modal-open');
    // Restaurar padding-right que bootstrap pudiera haber aplicado
    document.body.style.paddingRight = '';
  }

  // Remove bootstrap auto-switch attributes so data-api doesn't race with our JS.
  document.querySelectorAll('.modal-switcher').forEach(link => {
    // If you prefer to change templates instead, you can comment these two lines.
    link.removeAttribute('data-bs-toggle');
    link.removeAttribute('data-bs-dismiss');
  });

  // -------- main handler ----------
  document.querySelectorAll('.modal-switcher').forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      // Stop other handlers (bootstrap data-api listeners) from also responding
      e.stopPropagation();
      if (typeof e.stopImmediatePropagation === 'function') e.stopImmediatePropagation();

      const targetSelector = this.getAttribute('data-bs-target');
      if (!targetSelector) return;
      const targetModalEl = document.querySelector(targetSelector);
      if (!targetModalEl) return;

      const openModalEl = document.querySelector('.modal.show');

      // If there's an open modal, wait for it to fully hide, then open the target
      if (openModalEl) {
        const openInstance = bootstrap.Modal.getInstance(openModalEl) || new bootstrap.Modal(openModalEl);

        // Use a one-time handler
        const onHidden = function () {
          // Cleanup first (remove leftover backdrops & classes)
          cleanBackdropsAndBody();

          // Show the target
          const newModal = new bootstrap.Modal(targetModalEl);
          newModal.show();
        };

        openModalEl.addEventListener('hidden.bs.modal', onHidden, { once: true });
        openInstance.hide();

      } else {
        // No modal open -> open target directly (after cleaning in case of leftovers)
        cleanBackdropsAndBody();
        const newModal = new bootstrap.Modal(targetModalEl);
        newModal.show();
      }
    }, { passive: false });
  });

  // -------- keep cleanup robust: whenever any modal hides, remove stray backdrops --------
  document.querySelectorAll('.modal').forEach(modalEl => {
    modalEl.addEventListener('hidden.bs.modal', function () {
      // small delay to let bootstrap finish internal cleanup, then force-clean
      setTimeout(cleanBackdropsAndBody, 0);
    });
  });

  // Extra safety: on page click if there are multiple backdrops clean them
  // (helps if user triggers some weird sequence)
  document.addEventListener('click', function () {
    const backdrops = document.querySelectorAll('.modal-backdrop');
    if (backdrops.length > 1) cleanBackdropsAndBody();
  });

});

// Evita que el scroll del modal haga scroll en el body
document.addEventListener('shown.bs.modal', function (event) {
  const modalBody = event.target.querySelector('.modal-body');
  if (modalBody) {
    modalBody.addEventListener('wheel', function (e) {
      const { scrollTop, scrollHeight, clientHeight } = modalBody;
      const atTop = scrollTop === 0;
      const atBottom = scrollTop + clientHeight >= scrollHeight;

      if ((atTop && e.deltaY < 0) || (atBottom && e.deltaY > 0)) {
        e.preventDefault();
      }
    }, { passive: false });
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const backdrop = document.getElementById('custom-backdrop');

  function blockScroll(e) {
    const modal = document.querySelector('.modal.show');
    if (!modal) return;

    // Permitir scroll si el evento viene del modal
    const isInsideModal = modal.contains(e.target);
    if (!isInsideModal) {
      e.preventDefault();
    }
  }

  function showBackdrop() {
    backdrop.classList.add('show');
    document.body.style.overflow = 'hidden';
    document.documentElement.style.overflow = 'hidden';

    document.addEventListener('wheel', blockScroll, { passive: false });
    document.addEventListener('touchmove', blockScroll, { passive: false });
  }

  function hideBackdrop() {
    backdrop.classList.remove('show');
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';

    document.removeEventListener('wheel', blockScroll, { passive: false });
    document.removeEventListener('touchmove', blockScroll, { passive: false });
  }

  document.querySelectorAll('.modal').forEach(modalEl => {
    modalEl.addEventListener('shown.bs.modal', showBackdrop);
    modalEl.addEventListener('hidden.bs.modal', hideBackdrop);
  });

  backdrop.addEventListener('click', () => {
    const openModal = document.querySelector('.modal.show');
    if (openModal) {
      bootstrap.Modal.getInstance(openModal).hide();
    }
  });
});
