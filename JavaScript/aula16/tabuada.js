function tabuada() {
    let num = document.getElementById(`txtn`)
    let tab = document.getElementById(`seltab`)

    if (num.value.length == 0) {
        window.alert(`Por favor digite um número válido!`)
    } else {
        let n = Number(num.value)
        let c = 1

        tab.innerHTML = ``
        while (c < 11) {
            let item = document.createElement(`option`)
            item.text = `${n} x ${c} = ${n*c}`

            item.value = `tab${c}`

            tab.appendChild(item)
            c++
        }
    }
}