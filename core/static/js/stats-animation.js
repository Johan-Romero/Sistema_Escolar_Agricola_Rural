document.addEventListener('DOMContentLoaded', function () {
    const statsSection = document.querySelector('#estadisticas');
    const counters = document.querySelectorAll('[data-stat-target]');
    const animationDuration = 2000; // 2 seconds

    const animateCounter = (element) => {
        const target = +element.getAttribute('data-stat-target');
        let current = 0;
        const increment = target / (animationDuration / 16); // Approx. 60fps

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                element.innerText = Math.ceil(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                let finalValue = target.toLocaleString();
                if (target === 1000) {
                    finalValue += '+';
                }
                element.innerText = finalValue;
            }
        };
        updateCounter();
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                counters.forEach(counter => {
                    animateCounter(counter);
                });
                observer.unobserve(statsSection); // Stop observing after animation starts
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the element is visible
    });

    if (statsSection) {
        observer.observe(statsSection);
    }
});
