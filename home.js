const app = document.getElementById('typewriter');

const typewriter = new Typewriter(app, {
    loop: true,
    delay: 20
});
typewriter
    .typeString('Desarrollador Web')
    .pauseFor(1500)    // Espera 2 segundos
    .deleteAll()       // Borra todo
    .typeString('Full stack Developer')
    .pauseFor(1500)
    .deleteAll()
    .typeString('Desarrollador freelance') // Puedes agregar más
    .pauseFor(1500)
    .start();
