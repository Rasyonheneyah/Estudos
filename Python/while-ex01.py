print('Sistema de Avaliação de notas! Avalie essa frase a seguir:')
print('Toda proposição apresenta algum argumento, seja ele válido ou não')
nota=float(input('Insira uma nota: '))
while nota > 10 or nota<0:
    print('Valor inválido!')
    nota=float(input('Insira um valor entre 0 e 10: '))
if nota>=7.5:
    print('Uau! Você me deu uma nota boa!')
else:
    if 7.5>nota and nota>=5:
        print('Você me deu uma nota ok, valeu!')
    else:
        if nota<5:
            print('Minha nota foi ruim ;/')
print('--FIM--')