function fecharModal() {
    // Função para fechar o modal
    // Oculta o modal alterando o estilo de display
    document.getElementById('mensagemModal').style.display = 'none';
}

// Clicando no botao jogar
function iniciarJogo() {
    // Chama a mensagemModal
    document.getElementById('mensagemModal').style.display = 'block';
}

// Função para baixar o jogo
function baixarJogo() {
    fetch('http://127.0.0.1:5500/dist/forca.exe')
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'forca.exe';
            document.body.appendChild(a);
            a.click(); window.URL.revokeObjectURL(url);
        })
        .catch(() => alert('Falha ao baixar o arquivo!'));
    // Fecha o modal de informações
    fecharModal();
}

// Evento para fechar o modal se clicar fora dele
window.onclick = function (event) {
    let modal = document.getElementById('mensagemModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}