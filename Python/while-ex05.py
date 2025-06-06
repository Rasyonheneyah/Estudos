#leia 5 numeros e diga o maior, o menor, e a soma
soma=0
maior=0
menor=0
n1=int(input('Insira o primeiro numero'))
for i in range(5):
    n=int(input('Insira um numero: '))
    if n1<=n:
        menor=n1
    if n1<=n:
        maior=n1
    soma=n+soma
    n1=n
print(soma)
print(menor)
print(maior)