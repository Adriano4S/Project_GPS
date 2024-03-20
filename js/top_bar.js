document.addEventListener("DOMContentLoaded", function() {
    // Carregar o cabeçalho em um elemento com a classe "barra_supeior"
    var barraContainer = document.querySelector(".barra_supeior");
    if (barraContainer) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'barra_supeior.html', true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    barraContainer.innerHTML = xhr.responseText;
                } else {
                    console.error('Erro ao carregar o barra_supeior: ' + xhr.status);
                }
            }
        };
        xhr.send();
    } else {
        console.error('Elemento com classe "barra_supeior" não encontrado.');
    }
});
