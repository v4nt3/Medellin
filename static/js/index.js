const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const carousel = document.querySelector('.carousel-container');

let counter = 0;
const slideWidth = document.querySelector('.slide').clientWidth;

prevBtn.addEventListener('click', () => {
    counter--;
    if (counter < 0) {
        counter = document.querySelectorAll('.slide').length - 1;
    }
    carousel.style.transform = `translateX(${-slideWidth * counter}px)`;
});

nextBtn.addEventListener('click', () => {
    counter++;
    if (counter >= document.querySelectorAll('.slide').length) {
        counter = 0;
    }
    carousel.style.transform = `translateX(${-slideWidth * counter}px)`;
});
