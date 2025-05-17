

def soma(x,y):
    print(x+y)

def subtracao(x,y):
    print(x-y)

def multiplicacao(x,y):
    print(x*y)

def divisao(x,y):
    print(x/y)
    
def calculadora(x,y):
    soma(x,y)
    subtracao(x,y)
    multiplicacao(x,y)
    divisao(x,y)


x= int(input("Digite X: "))
y= int(input("Digite Y: "))
calculadora(x,y)
