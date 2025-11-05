'''
Exercício 3:
Faça um programa que leia um número inteiro e mostre na tela o
seu antecessor e seu sucessor.
'''
lista = ('Antecessor', 'Número: ', 'Sucessor: ')
def nEntre(a):
    print(f'Antecessor: {(a-1)}\nNúmero: {a}\nSucessor: {a+1}')


n1 = int(input('Insira um número: '))
nEntre(n1)
