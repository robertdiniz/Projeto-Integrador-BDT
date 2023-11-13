modalBiografia = document.querySelector('.modal-bio');
fade = document.querySelector('.fade');

function modalBio(){
    modalBiografia.classList.toggle('modal-active-bio')
    fade.classList.toggle('modal-active-bio');
    console.log(modalBiografia);
}