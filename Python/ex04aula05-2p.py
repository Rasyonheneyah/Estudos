'''
Exercício 4:
Crie uma aplicação que leia um número e mostre seu dobro, seu
triplo e a sua raiz quadrada
'''

import math


def dtr(n):
    print(f'Dobro: {n*2}')
    print(f'Triplo: {n*3}')
    print(f'Raíz quadrada: {n**0.5}')
    print(math.sqrt(n))
n1 = dtr(int(input('Insira um número: ')))
