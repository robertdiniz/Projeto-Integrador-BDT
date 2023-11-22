fade = document.querySelector('.fade');
modal = document.querySelector('.modal');

function enviarRepositorio(moduloSelecionado){
    exibirModalRepositorio(moduloSelecionado);
}

function exibirModalRepositorio(moduloSelecionado){
    fade.classList.toggle('modal-active');
    modal.classList.toggle('modal-active');

    document.getElementById("modulo_selecionado").value = moduloSelecionado;
    document.getElementById("submit-rep").addEventListener("click", function() {
        document.getElementsByClassName("form-submit-rep").submit();
    });
}