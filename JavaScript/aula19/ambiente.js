function parimp(n) {
    if (n%2 ==0){
        return `par`
        
    } else {
        return `impar`
    }
}

let res = parimp(11)
console.log(res)

let lista = [1, 2, 3, 4, 5, 6, 7, 8]
for (let i in lista) {
    console.log(`O número ${lista[i]} é ${parimp(lista[i])} `)
}