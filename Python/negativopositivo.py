'''
4.Fazer uma função que recebe um argumento inteiro. A 
função retorna o valor de caractere ‘P’, se seu 
argumento for positivo, e ‘N’, se seu argumento for 
zero ou negativo.
'''
def p_n(num):
    if num > 0:
        return 'P'
    elif num == 0:
        return 'Z'
    else:
        return 'N'
for i in range(5):
    
    print(f'{i} : {p_n(i)}')

