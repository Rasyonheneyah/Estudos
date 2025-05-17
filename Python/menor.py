valor = int(input("Insira valor: "))
menor = valor
while valor != -1:
    if valor < menor:
        menor= valor
    valor=int(input("Insira outro valor: "))
print("O menor valor e ", menor)
