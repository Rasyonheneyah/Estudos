'''8.Crie uma função que receba duas palavras e retorne 
True caso a primeira palavra seja um prefixo da 
segunda. Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ 
não é prefixo de ’uf’.
'''
p1 = input('Primeira Palavra: ')
p2 = input('Segunda Palavra: ')


def verificar_prefixo(p1,p2):
    '''
    Para onde eu tava encaminhando, daria um trabalhão desnecessário...
    if len(p1) < len(p2):
        pmenor = len(p1)
    else:
        pmenor  len(p2)
    for i in range(pmenor):
        if
    '''

    
    if p1.lower() == p2.lower():
        print('Boa tentativa, mas você digitou a mesma palavra.')
    elif p1.lower() in p2[0:len(p1)].lower():
        print(f'`{p1}` é prefixo de `{p2}` ') 
    else:
        print(f'`{p1}` não é prefixo de `{p2}` ')
        
verificar_prefixo(p1,p2)


# Resolução do professor
'''
def prefixo(p1, p2):
    if len(p1) < len(p2):
        if p1==p2[:len(p1)]:
            if p1.lower() == p2[:len(p1)].lower():
                print('é prefixo')
                return True
            else:
                print('n e prefixo')
                return False
        
# prefixo(p1, p2)
'''
