# Jogadores
SomaJogadores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Contagem_de_votos = 0
flag = True
while flag:
    numjogador = int(input('Insira um valor entre 1 a 23 para votar nos jogadores respectivos ao número de sua camisa.\nCaso queira sair, digite 0.\n'))
    if numjogador == 0:
        flag = False
    elif numjogador > 23 or numjogador < 0 or numjogador == str or numjogador == float or numjogador == bool:
        print('INSIRA UM NÚMERO VÁLIDO.')
    else:
        numjogador = numjogador - 1
        SomaJogadores[numjogador] = SomaJogadores[numjogador] + 1
        print(f'\n=== VOTO COMPUTADO! ===\n')
        Contagem_de_votos = Contagem_de_votos + 1
print(SomaJogadores)
c = 1
for i in SomaJogadores:
    print(f'Jogador número:  {c}: {i} Votos')
    c = c + 1
print(f'Foram apurados {Contagem_de_votos} votos!')
