// ==============================
// INITIALIZATION
// ==============================

const slides = document.querySelectorAll(".slide");

const previousBtn = document.getElementById("previousBtn");
const nextBtn = document.getElementById("nextBtn");
const fullscreenBtn = document.getElementById("fullscreenBtn");

const currentSlideDisplay = document.getElementById("currentSlide");
const totalSlidesDisplay = document.getElementById("totalSlides");

let currentSlide = 0;

const totalSlides = slides.length;


// ==============================
// DISPLAY SLIDE
// ==============================

function displaySlide() {

    slides.forEach((slide, index) => {

        slide.classList.remove("active");

        if (index === currentSlide) {
            slide.classList.add("active");
        }

    });


    // Update slide counter

    currentSlideDisplay.textContent =
        String(currentSlide + 1).padStart(2, "0");

    totalSlidesDisplay.textContent =
        String(totalSlides).padStart(2, "0");


    // Update button states

    previousBtn.disabled = currentSlide === 0;

    nextBtn.disabled = currentSlide === totalSlides - 1;

}


// ==============================
// NEXT SLIDE
// ==============================

function nextSlide() {

    if (currentSlide < totalSlides - 1) {

        currentSlide++;

        displaySlide();

    }

}


// ==============================
// PREVIOUS SLIDE
// ==============================

function previousSlide() {

    if (currentSlide > 0) {

        currentSlide--;

        displaySlide();

    }

}


// ==============================
// BUTTON EVENTS
// ==============================

nextBtn.addEventListener("click", nextSlide);

previousBtn.addEventListener("click", previousSlide);


// ==============================
// KEYBOARD NAVIGATION
// ==============================

document.addEventListener("keydown", (event) => {

    if (event.key === "ArrowRight" || event.key === "ArrowDown") {

        nextSlide();

    }

    else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {

        previousSlide();

    }

    else if (event.key.toLowerCase() === "f") {

        toggleFullscreen();

    }

});


// ==============================
// FULLSCREEN
// ==============================

function toggleFullscreen() {

    if (!document.fullscreenElement) {

        document.documentElement.requestFullscreen();

    }

    else {

        document.exitFullscreen();

    }

}


fullscreenBtn.addEventListener("click", toggleFullscreen);


// ==============================
// INITIAL DISPLAY
// ==============================

displaySlide();