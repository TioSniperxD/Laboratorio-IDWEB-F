function mostrarInfo(idCategoria, tarjetaClickeda) {
    const yaEstabaActiva = tarjetaClickeda.classList.contains('active');

    const contenidos = document.querySelectorAll('.content-box');
    contenidos.forEach(caja => {
        caja.classList.remove('active-content');
    });

    const tarjetas = document.querySelectorAll('.card');
    tarjetas.forEach(card => {
        card.classList.remove('active');
    });

    if (!yaEstabaActiva) {
        document.getElementById(idCategoria).classList.add('active-content');
        tarjetaClickeda.classList.add('active');
    }
}