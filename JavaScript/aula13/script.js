function carregar() {
    var msg = window.document.getElementById(`msg`)
    var img = window.document.getElementById(`imagem`)
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 6 && hora <= 12) {
        //bom dia
        img.src = `./img/manha.jpg`
        document.body.style.background = "#E6F7FF"
    } else if (hora > 12 && hora < 19) {
        // boa tarde
        img.src = `./img/tarde.jpg`
        document.body.style.background = "#FFE5B4"

    } else if (hora >= 19 || hora < 6) {
        //boa noite
        img.src = `./img/noite.jpg`
        document.body.style.background = "#1A1A2E"
    }

}
