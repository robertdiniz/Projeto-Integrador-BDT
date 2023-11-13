modal = document.querySelector('.modal-photo');
fade = document.querySelector('.fade');
trocarImagemDiv = document.querySelector('.fade-trocar-imagem-form');

function modalPhoto(){
    modal.classList.toggle('modal-active-photo');
    fade.classList.toggle('modal-active-photo');
    trocarImagemDiv.classList.toggle('modal-active-photo');
}