function contagem() {
    var ini = document.getElementById(`txtini`)
    var fim = document.getElementById(`txtfim`)
    var pas = document.getElementById(`txtpas`)
    var res = document.getElementById('res')

    if (ini.value.length == 0 || fim.value === '' || pas.value === '') {
        alert('Por favor, preencha todos os campos: início, fim e passo.')
    } else if (pas.value === '0')
    {
        alert(`Insira um valor diferente de 0 nos passos.`)
    }
    
    var inicio = Number(ini.value)
    var final = Number(fim.value)
    var passos = Number(pas.value)
    
    if (inicio > final) {
        if (inicio + passos < final) {
            alert(`Por favor, preencha o passo adequadamente. É necessário que seja possível realizar ao menos um passo.`)
            return
        }

    } else if (inicio + passos > final) {
        alert(`Por favor, preencha o passo adequadamente. É necessário que seja possível realizar ao menos um passo.`)
        return
    }
    
    res.innerHTML = 'Contando...'  // limpa antes de começar
    if (passos <= 0) {
        passos = 1
    }
    if (inicio < final) {
        // Contagem crescente
        for (let i = inicio; i <= final; i += passos) {
            res.innerHTML +=   `<span class="espaco">&#x1F9B6; Passo = ${i} \u{1f603}</span>`
        }
    } else {
        // Contagem decrescente
        for (let i = inicio; i >= final; i -= passos) {
            res.innerHTML += `<span class='espaco'>&#x1F9B6; Passo = ${i} \u{1f603}</span>`
        }

    }
    res.innerHTML += `\u{1f3c1}`
}

