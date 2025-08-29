let amigo = {
    nome: `José`,
    peso: 67.4,
    engordar(p=0) {
        console.log(`Engordou`)
        this.peso += p
    }
}
amigo.engordar(1.5)
console.log(`${amigo.nome} pesa ${amigo.peso} Kg`)