'Salto a distancia cada atelta tem 5 saltos.'
ordem_saltos = {
    0: 'Primeiro',
    1:'Segundo',
    2:'Terceiro',
    3:'Quarto',
    4:'Quinto',
}


    atlnome = input('Insira o nome do atleta: ')
    saltos = []
    for i in range(5):
        salto = float(input(f'Valor do {ordem_saltos[i]} salto: '))
        saltos.append(salto)
    saida()
    print(saltos)
    print(f'Atleta: {atlnome}')
    for i in range(5):
        print(f'{ordem_saltos[i]} salto: {saltos[i]}')
    print(f'Resultado Final: \nAtleta: {atlnome}\nSaltos: ', *saltos)
