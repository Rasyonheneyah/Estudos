'''8.Crie uma função que receba duas palavras e retorne 
True caso a primeira palavra seja um prefixo da 
segunda. Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ 
não é prefixo de ’uf’.
'''

verificador = False
print('Insira duas palavras, vejamos se uma e prefixo da outra.')
p1 = input('Primeira Palavra: ')
p2 = input('Segunda Palavra: ')


'''
if len(p1) < len(p2):
    pmenor = len(p1)
else:
    pmenor  len(p2)
for i in range(pmenor):
    if
'''

if p1 in p2[0:]:
    print(f'`{p1}` é prefixo de `{p2}` ')
else:
    print(f'`{p1}` não é prefixo de `{p2}` ')
