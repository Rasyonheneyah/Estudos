let num = [5, 8 ,9 , 3]

console.log(`Nosso vetor é o ${num}`, num)

num[4] = 6
console.log(`O ${num[3]} foi adicionado ao nosso vetor!`)

num.push(5)
console.log(`O ${num[5]} foi adicionado diretamente no último lugar em nosso índice!`)

console.log(`${num.length}`)

num.sort()
console.log(`Nosso vetor em ordem crescente ficou ${num}`)

for (var i = 0; i !== num.length; i++ ) {
    console.log(`O elemento ${num[i]} tem o índice ${i}`)

}

for (let pos in num){
    console.log(`${num[pos]} -> ${pos}`)
}

console.log(`${num.indexOf(5)} ${num.indexOf(10)}`)

teste = [10, 3, 220, 41, 23]
console.log(teste)
console.log(teste.sort())