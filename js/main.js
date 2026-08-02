document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');

            // Animate hamburger
            const spans = hamburger.querySelectorAll('span');
            spans[0].classList.toggle('rotate-left');
            spans[1].classList.toggle('opacity-0');
            spans[2].classList.toggle('rotate-right');
        });
    }

    // Smooth scroll for internal links.
    // Skip the villa filter buttons (they manage the page themselves) and
    // guard against anchors whose target doesn't exist on the page.
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.classList.contains('villa-filter') || this.classList.contains('villa-filter-reset')) return;
            const target = document.querySelector(this.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Header shadow once the page is scrolled
    const header = document.querySelector('header');
    if (header) {
        const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 10);
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // ---- Scroll-reveal motion ----------------------------------------
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion || !('IntersectionObserver' in window)) return;

    // Hero content rises on page load
    document.querySelectorAll('.hero-content').forEach(el => el.classList.add('hero-entrance'));

    // Elements that fade up as they scroll into view
    const targets = document.querySelectorAll([
        '.section-title',
        '.villa-grid > *',
        '.villa-gallery img',
        'main section.container > div > p',
        'main section.container > div > h2',
    ].join(', '));

    // Stagger siblings that share a parent so grids cascade in
    const perParent = new Map();
    targets.forEach(el => {
        if (el.closest('.hero-content')) return;
        const n = perParent.get(el.parentElement) || 0;
        perParent.set(el.parentElement, n + 1);
        el.style.setProperty('--reveal-delay', `${Math.min(n, 5) * 80}ms`);
        el.classList.add('reveal');
    });

    const io = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                io.unobserve(entry.target);
            }
        });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    // Anything already in the viewport on load reveals immediately —
    // and as a safety net, never leave content hidden if the observer misfires.
    setTimeout(() => {
        document.querySelectorAll('.reveal:not(.in-view)').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in-view');
        });
    }, 250);
});
