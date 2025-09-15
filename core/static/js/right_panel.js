document.addEventListener("DOMContentLoaded", function () {
  /* ---------- Calendario simple (render en grid) ---------- */
  const calendarEl = document.getElementById("calendar");
  const titleEl = document.getElementById("calendarTitle");
  const prevBtn = document.getElementById("prevMonth");
  const nextBtn = document.getElementById("nextMonth");

  let today = new Date();
  let currentYear = today.getFullYear();
  let currentMonth = today.getMonth(); // 0-index

  function renderCalendar(year, month) {
    titleEl.textContent = new Date(year, month).toLocaleString('default', { month: 'long', year: 'numeric' });

    // build header weekdays
    const weekdays = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    const header = document.createElement('div');
    header.className = 'weekdays';
    weekdays.forEach(d => {
      const el = document.createElement('div');
      el.className = 'weekday';
      el.textContent = d;
      header.appendChild(el);
    });

    // build days grid
    const daysGrid = document.createElement('div');
    daysGrid.className = 'days';

    // first day info
    const firstDay = new Date(year, month, 1);
    const startDayIndex = firstDay.getDay(); // 0..6
    // previous month days to fill preceding cells
    const prevMonthLastDay = new Date(year, month, 0).getDate();

    // number of days in this month
    const daysInMonth = new Date(year, month+1, 0).getDate();

    // fill trailing days from prev month
    for (let i = startDayIndex - 1; i >= 0; i--) {
      const d = prevMonthLastDay - i;
      const cell = document.createElement('div');
      cell.className = 'day outside';
      cell.textContent = d;
      daysGrid.appendChild(cell);
    }

    // fill current month
    for (let d = 1; d <= daysInMonth; d++) {
      const cell = document.createElement('div');
      cell.className = 'day';
      cell.textContent = d;
      // highlight today
      if (year === today.getFullYear() && month === today.getMonth() && d === today.getDate()) {
        cell.classList.add('today');
      }
      daysGrid.appendChild(cell);
    }

    // fill next month days to complete grid (optional)
    const totalCells = startDayIndex + daysInMonth;
    const nextFill = (totalCells % 7 === 0) ? 0 : (7 - (totalCells % 7));
    for (let i = 1; i <= nextFill; i++) {
      const cell = document.createElement('div');
      cell.className = 'day outside';
      cell.textContent = i;
      daysGrid.appendChild(cell);
    }

    // clear and append
    calendarEl.innerHTML = '';
    calendarEl.appendChild(header);
    calendarEl.appendChild(daysGrid);
  }

  prevBtn.addEventListener('click', function () {
    currentMonth--;
    if (currentMonth < 0) { currentMonth = 11; currentYear--; }
    renderCalendar(currentYear, currentMonth);
  });

  nextBtn.addEventListener('click', function () {
    currentMonth++;
    if (currentMonth > 11) { currentMonth = 0; currentYear++; }
    renderCalendar(currentYear, currentMonth);
  });

  renderCalendar(currentYear, currentMonth);
});

