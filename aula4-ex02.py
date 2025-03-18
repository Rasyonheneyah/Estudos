# Fala qual o menor valor de um conjunto de valores.
Valor=int(input('Insira algum valor:'))
Menor=Valor
while Valor!=-1:
    if Valor<Menor:
        Menor=Valor
    Valor=int(input('Insira outro valor:'))
print('O menor valor e', Menor) 
