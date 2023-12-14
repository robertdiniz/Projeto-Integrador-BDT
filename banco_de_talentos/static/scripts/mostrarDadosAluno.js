fade = document.querySelector('.fade');
modal = document.querySelector('.modal');
nome_completo_p = document.querySelector('.nome-completo-aluno');
email_aluno_p = document.querySelector('.email-aluno');
matricula_aluno_img = document.querySelector('.matricula-aluno-request');
titulo_modal = document.querySelector('.title-modal-aluno');
active_account = document.querySelector('.active-account');
reject_account = document.querySelector('.reject-account');
form = document.querySelector('.confirm-account');

let emailAluno;

function mostrarDadosAluno(nome_usuario, nome_aluno, email_aluno, matricula_aluno){
    fade.classList.toggle('modal-active');
    modal.classList.toggle('modal-active');
    nome_completo_p.textContent = nome_aluno;
    email_aluno_p.textContent = email_aluno;
    matricula_aluno_img.href = matricula_aluno;
    titulo_modal.textContent = `Dados do usuário ${nome_usuario}`;
    emailAluno = email_aluno;
}

function aceitar(){
    active_account.value = emailAluno;
    form.submit();
}

function rejeitar(){
    reject_account.value = emailAluno;
    form.submit();
}



