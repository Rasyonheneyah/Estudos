# ValorPagamento -> valor a ser pago por uma prestação de uma conta
# atraso -> atraso em dias
#

def ValorPagamento(p,a):
    if a!=0:
        p= (p*1.03)+ (0.001*a)
    print(f'O valor a ser pago é R${p}')
    lista.append(p)
    return p

total=0
lista=[]
prestacao=0
atraso=0
flag= True
while flag:
    prestacao= int(input("Insira a Prestação: "))
    if prestacao==0:
        flag=False
    else:
        
        atraso=  int(input("Insira o Atraso: "))

        ValorPagamento(prestacao, atraso)
qntd= len(lista)
print("PRESTAÇÕES")
print("Qtd   |  Valor")
for i in range(qntd):
    print(i+1,lista[i])
    total= lista[i] + total
print(f'Total |  {total}')
