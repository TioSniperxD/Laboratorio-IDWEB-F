
const form = document.getElementById('contactForm');
const errorMsg = document.getElementById('errorMsg');

form.addEventListener('submit', function (e) {
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const asunto = document.getElementById('asunto').value;

    if (nombre === "" || correo === "" || asunto === "") {
        e.preventDefault();
        errorMsg.style.display = 'block';
    } else {
        errorMsg.style.display = 'none';
    }
});
