modal = document.querySelector('.modal');
fade = document.querySelector('.fade');
modalSocial = document.querySelector('#modal-container-form');

function mostrarModal(){
    modal.classList.toggle('modal-active');
    fade.classList.toggle('modal-active');
    modalSocial.classList.toggle('modal-active');
}