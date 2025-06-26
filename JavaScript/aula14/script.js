function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById(`txtano`)
    var res = document.getElementById(`res`)

    if (fano.value.length < 4 || Number(fano.value) > ano) {
        window.alert(`[ERRO] Verifique os dados e tente novamente!`)
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''

        var img = document.createElement(`img`)
        img.setAttribute(`id`, `foto`)

        if (fsex[0].checked) {
            gênero = 'Homem'

            if (idade >= 0 && idade < 12) {
                //criança
                img.setAttribute(`src`, `./img/bebeh.jpg`)

            } else if (idade > 12 && idade <= 25) {
                // jovem
                img.setAttribute(`src`, `./img/jovemh.jpg`)

            } else if (idade > 26 && idade < 50) {
                // adulto
                img.setAttribute(`src`, `./img/h.jpg`)
            } else if (idade >= 50) {
                // idoso
                 img.setAttribute(`src`, `./img/idoso.jpg`)
                
            }

        } else if (fsex[1].checked) {
            gênero = 'Mulher'
        
            if (idade >= 0 && idade < 12) {
                //criança
                img.setAttribute(`src`, `./img/bebem.jpg`)

            } else if (idade > 12 && idade <= 25) {
                // jovem
                img.setAttribute(`src`, `./img/jovemm.jpg`)
                
            } else if (idade > 26 && idade < 50) {
                // adulta
                img.setAttribute(`src`, `./img/m.jpg`)

            } else if (idade >= 50) {
                // idosa
                img.setAttribute(`src`, `./img/idosa.jpg`)

            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
    }   

    
}