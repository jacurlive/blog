'use strict';

document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');

    darkModeToggle.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
        darkModeToggle.classList.toggle('dark-mode');
    });
});

function openFullScreen(img) {
    const modal = document.getElementById("myModal");
    const modalImg = document.getElementById("img01");
    modal.style.display = "block";
    modalImg.src = img.src;
}

function closeFullScreen() {
    document.getElementById("myModal").style.display = "none";
}

const modal = document.getElementById("myModal");
const modalImg = document.getElementById("img01");

function openFullScreen(img) {
    modal.style.display = "block";
    modalImg.src = img.src;

    modal.addEventListener("click", closeFullScreen);

    document.addEventListener("keydown", function(event) {
        if (event.key === "Escape") {
            closeFullScreen();
        }
    });
}

function closeFullScreen() {
    modal.style.display = "none";

    modal.removeEventListener("click", closeFullScreen);

    document.removeEventListener("keydown", function(event) {
        if (event.key === "Escape") {
            closeFullScreen();
        }
    });
}