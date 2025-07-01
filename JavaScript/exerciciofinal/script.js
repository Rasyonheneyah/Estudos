numeros = []
let iteradorl = 0
let lisn = document.getElementById(`listan`)
let num = document.getElementById(`txtn`)
let res = document.getElementById(`res`)
let acionado = 0

lisn.innerText = ``

function adicionar() {

    if (num.length == 0 || num.value < 1 || num.value > 100 ) {
        alert(`Insira um número válido!`)
        return
    }

    for (let i in numeros) {
        if (num.value == numeros[i]) {
            alert(`Não coloque um número repetido!`)   
            return 
        }
    } 
    let item = document.createElement(`option`)
    item.text = `Valor ${num.value} adicionado.`
    iteradorl++
    item.value = `listan${iteradorl}`
    lisn.appendChild(item)
    numeros.push(Number(num.value))
    
}

// Funções para o resultado
function maior() {
    let mais = 0
    for (let i in numeros) {
        if (numeros[i] > mais) {
            mais = numeros[i]
        }
        
    }
    return mais
}
function menor() {
    let menos = numeros [0]
    for (let i in numeros) {
        if (numeros[i] < menos) {
            menos = numeros[i]
        }
    }
    return menos
}
function somar() {
    let soma = 0
    for (let i in numeros) {
        soma += numeros[i]
    }
    return soma
}
function media() {
    let somas = somar()
    let media = somas/numeros.length
    return media
}
function zerar() {
    numeros = []
    lisn.innerText = ""
    res.innerHTML = ""
    acionado = 0
}

function finalizar() {
    if (numeros.length == 0) {
        alert('Adicione números à lista antes de finalizar.')
    } else if (acionado == 0) {
            
    
        let tot = numeros.length
        res.innerHTML += `<p>Temos um total de ${tot} números cadastrados na lista.</p>`

        let mai = maior()
        res.innerHTML += `<p>O maior número da lista é o ${mai}.</p>`

        let men = menor()
        res.innerHTML += `<p>Já o menor número é o ${men}.</p>`

        let som = somar()
        res.innerHTML += `<p>A soma de todos os números resulta em ${som}.</p>`

        let med = media()
        res.innerHTML += `<p>A média de todos os números enviados é de ${med}.</p>`
        
        acionado = 1 
    } else if (acionado = 1){
        alert(`Você precisa zerar para finalizar novamente.`)
    }
}