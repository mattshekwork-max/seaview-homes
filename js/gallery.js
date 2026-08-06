// Seaview Homes - Popup Photo Gallery
// Drop into any villa page. Add class "gallery-img" to thumbnails inside a container with id "villa-gallery".
// The script auto-collects images, builds the lightbox, handles nav, keyboard, and touch swipe.

(function () {
    var images = [];
    var current = 0;

    function init() {
        var container = document.getElementById('villa-gallery');
        if (!container) return;

        var thumbs = container.querySelectorAll('img.gallery-img');
        thumbs.forEach(function (thumb, i) {
            images.push({ src: thumb.src, alt: thumb.alt });
            thumb.addEventListener('click', function () { openGallery(i); });
            thumb.style.cursor = 'pointer';
        });

        buildLightbox();
    }

    function buildLightbox() {
        var overlay = document.createElement('div');
        overlay.id = 'gallery-overlay';
        overlay.style.cssText = 'display:none;position:fixed;inset:0;background:rgba(0,0,0,0.92);z-index:9999;align-items:center;justify-content:center;opacity:0;transition:opacity 0.3s ease;';

        var closeBtn = document.createElement('span');
        closeBtn.innerHTML = '&times;';
        closeBtn.style.cssText = 'position:absolute;top:1.2rem;right:1.8rem;color:#fff;font-size:2.5rem;cursor:pointer;line-height:1;user-select:none;opacity:0.8;transition:opacity 0.2s;';
        closeBtn.onmouseenter = function () { this.style.opacity = '1'; };
        closeBtn.onmouseleave = function () { this.style.opacity = '0.8'; };
        closeBtn.onclick = closeGallery;
        overlay.appendChild(closeBtn);

        var prevBtn = document.createElement('span');
        prevBtn.innerHTML = '&#10094;';
        prevBtn.style.cssText = 'position:absolute;left:1.5rem;top:50%;transform:translateY(-50%);color:#fff;font-size:2.5rem;cursor:pointer;user-select:none;opacity:0.6;transition:opacity 0.2s;padding:1rem;';
        prevBtn.onmouseenter = function () { this.style.opacity = '1'; };
        prevBtn.onmouseleave = function () { this.style.opacity = '0.6'; };
        prevBtn.onclick = function (e) { e.stopPropagation(); prevImage(); };
        overlay.appendChild(prevBtn);

        var nextBtn = document.createElement('span');
        nextBtn.innerHTML = '&#10095;';
        nextBtn.style.cssText = 'position:absolute;right:1.5rem;top:50%;transform:translateY(-50%);color:#fff;font-size:2.5rem;cursor:pointer;user-select:none;opacity:0.6;transition:opacity 0.2s;padding:1rem;';
        nextBtn.onmouseenter = function () { this.style.opacity = '1'; };
        nextBtn.onmouseleave = function () { this.style.opacity = '0.6'; };
        nextBtn.onclick = function (e) { e.stopPropagation(); nextImage(); };
        overlay.appendChild(nextBtn);

        var imgWrap = document.createElement('div');
        imgWrap.style.cssText = 'display:flex;flex-direction:column;align-items:center;max-width:90%;max-height:90%;';

        var img = document.createElement('img');
        img.id = 'gallery-img';
        img.style.cssText = 'max-width:90vw;max-height:80vh;border-radius:6px;box-shadow:0 8px 32px rgba(0,0,0,0.6);object-fit:contain;transition:opacity 0.25s ease;';
        imgWrap.appendChild(img);

        var counter = document.createElement('p');
        counter.id = 'gallery-counter';
        counter.style.cssText = 'color:#fff;font-size:0.95rem;margin-top:0.8rem;opacity:0.7;font-family:Georgia,serif;';
        imgWrap.appendChild(counter);

        overlay.appendChild(imgWrap);

        // Click outside image to close
        overlay.addEventListener('click', function (e) {
            if (e.target === overlay || e.target === imgWrap) closeGallery();
        });

        document.body.appendChild(overlay);

        // Keyboard
        document.addEventListener('keydown', function (e) {
            if (overlay.style.display === 'none') return;
            if (e.key === 'Escape') closeGallery();
            if (e.key === 'ArrowLeft') prevImage();
            if (e.key === 'ArrowRight') nextImage();
        });

        // Touch swipe
        var touchStartX = 0;
        var touchEndX = 0;
        overlay.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
        });
        overlay.addEventListener('touchend', function (e) {
            touchEndX = e.changedTouches[0].screenX;
            var diff = touchStartX - touchEndX;
            if (Math.abs(diff) > 50) {
                if (diff > 0) nextImage();
                else prevImage();
            }
        });
    }

    function openGallery(index) {
        current = index;
        var overlay = document.getElementById('gallery-overlay');
        overlay.style.display = 'flex';
        overlay.style.opacity = '0';
        requestAnimationFrame(function () {
            overlay.style.opacity = '1';
        });
        document.body.style.overflow = 'hidden';
        showImage();
    }

    function showImage() {
        var img = document.getElementById('gallery-img');
        var counter = document.getElementById('gallery-counter');
        img.style.opacity = '0';
        img.src = images[current].src;
        img.alt = images[current].alt;
        img.onload = function () { img.style.opacity = '1'; };
        counter.textContent = (current + 1) + ' of ' + images.length;
    }

    function nextImage() {
        current = (current + 1) % images.length;
        showImage();
    }

    function prevImage() {
        current = (current - 1 + images.length) % images.length;
        showImage();
    }

    function closeGallery() {
        var overlay = document.getElementById('gallery-overlay');
        overlay.style.opacity = '0';
        setTimeout(function () {
            overlay.style.display = 'none';
            document.body.style.overflow = '';
        }, 300);
    }

    // Auto-init on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();