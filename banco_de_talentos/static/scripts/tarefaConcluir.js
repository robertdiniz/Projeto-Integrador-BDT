checkbox_custom = document.querySelector('.checkbox-personalizado');
form = document.querySelector('.form-task');
task_concluida = document.querySelector('.task-concluida');

function concluirTarefa(tarefa){
    task_concluida.value = tarefa;
    form.submit();
};
