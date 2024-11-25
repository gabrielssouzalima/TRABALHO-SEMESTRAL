document.querySelectorAll('.btnPalavra').forEach(button => { /* Seleciona todos os elementos da classe */
    const audio = new Audio(button.dataset.audio); 
    button.onmouseover = () => audio.play(); // Toca o áudio quando o mouse passa
});