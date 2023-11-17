fade = document.querySelector('.fade');
modal = document.querySelector('.modal');

function escolherTrilha(trilhaSelecionada){
    exibirModalTrilha(trilhaSelecionada);
}

function exibirModalTrilha(trilhaSelecionada){
    fade.classList.toggle('modal-active');
    modal.classList.toggle('modal-active');

    document.getElementById("trilha_selecionada").value = trilhaSelecionada;
    document.getElementById("fazer-trilha").addEventListener("click", function() {
        document.getElementById("form-trilha").submit();
    });
}