var agora = new Date()
var hora = agora.getHours()

console.log(`Agora são exatamente ${hora} horas`)
if (hora <= 12 && hora > 5) {
    console.log(`Bom dia!`)
}
else if (hora > 12) {
    console.log(`Boa tarde!`)
}
else if (hora >= 19 || hora < 6) {
    console.log(`Boa noite!`)
}