# Verificador de Triangulo se é Equilátero, Isóceles ou Escalenos
l1=float(input('Insira o primeiro lado:'))
l2=float(input('Insira o segundo lado:'))
l3=float(input('Insira o terceiro lado:'))
if l1==l2==l3:
    print('O Triângulo é Equilátero, pois possui todos os lados iguais.')
else:
    if (l1==l2 or l1==l3 or l2==l3) and (l1,l2!=l3 or l1,l3!=l2 or l2,l3!=l1):
        print('O Triângulo é Isóceles pois possui dois lados iguais.')
    else:
        if l1!=l2!=l3:
            print('O Triângulo é Escaleno, pois todos seus lados são diferentes')
            