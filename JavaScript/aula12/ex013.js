var agora = new Date()
var diaSem = agora.getDay()

/*
0 Dom / 1 Seg / 2 Ter / 3 Qua / 4 QUi / 5 Sex / 6 Sab
*/

switch (diaSem) {
    case 0:
        console.log(`Domingo`)
        break
    case 1:
        console.log(`Segunda`)
        break
        case 2:
        console.log(`Terça`)
        break
    case 3:
        console.log(`Quarta`)
        break
    case 4:
        console.log(`Quinta`)
        break
    case 5:
        console.log(`Sexta`)
        break
    default:
        console.log(`Sábado`)
        break
    }    
console.log(diaSem)
    


