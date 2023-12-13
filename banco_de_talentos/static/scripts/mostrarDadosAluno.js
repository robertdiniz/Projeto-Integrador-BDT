fade = document.querySelector('.fade');
modal = document.querySelector('.modal');
nome_completo_p = document.querySelector('.nome-completo-aluno');
email_aluno_p = document.querySelector('.email-aluno');
matricula_aluno_img = document.querySelector('.matricula-aluno-request');
active_account = document.querySelector('.active-account');
reject_account = document.querySelector('.reject-account');
titulo_modal = document.querySelector('.title-modal-aluno');

function mostrarDadosAluno(nome_usuario, nome_aluno, email_aluno, matricula_aluno){
    fade.classList.toggle('modal-active');
    modal.classList.toggle('modal-active');
    nome_completo_p.textContent = nome_aluno;
    email_aluno_p.textContent = email_aluno;
    matricula_aluno_img.href = matricula_aluno;
    active_account.value = email_aluno;
    reject_account.value = email_aluno;
    titulo_modal.textContent = `Dados do usuário ${nome_usuario}`;
}



