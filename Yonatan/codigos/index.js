const main_img = document.querySelector('.main_img');
const thumbnails = document.querySelectorAll('.thumbnail');
const interval = 5000;
let currentIndex = 0;

function changeImage(index) {
    const active = document.querySelector('.active');
    active.classList.remove('active');
    thumbnails[index].classList.add('active');
    main_img.src = thumbnails[index].src;
    
    // Agregar un retraso para la transición de opacidad
    setTimeout(() => {
        active.style.opacity = 0.7;
        thumbnails[index].style.opacity = 1;
    }, 100);
}

function nextImage() {
    currentIndex = (currentIndex + 1) % thumbnails.length;
    changeImage(currentIndex);
}

function openImageOverlay(index) {
    const enlargedImage = document.getElementById('enlarged-image');
    enlargedImage.src = thumbnails[index].src;
    const imageOverlay = document.querySelector('.image-overlay');
    imageOverlay.style.display = 'block';
}

function closeImageOverlay() {
    const imageOverlay = document.querySelector('.image-overlay');
    imageOverlay.style.display = 'none';
}

thumbnails.forEach((thumb, index) => {
    thumb.addEventListener('click', function() {
        openImageOverlay(index);
    });
});

setInterval(nextImage, interval);