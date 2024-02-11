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
