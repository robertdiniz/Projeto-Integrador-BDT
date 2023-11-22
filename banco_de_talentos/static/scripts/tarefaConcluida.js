document.getElementById('meu-checkbox').addEventListener('change', function(event) {
    const isChecked = event.target.checked;
    // Enviar o status do checkbox para o servidor usando AJAX
    fetch('/atualizar_checkbox/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ isChecked: isChecked }),
    })
    .then(response => response.json())
    .then(data => console.log(data)) // Exibir resposta do servidor no console
    .catch(error => console.error('Erro:', error));
  });