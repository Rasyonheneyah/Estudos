a=int(input('Insira um número: '))
b=int(input('Insira outro número MENOR:'))
while b>=a:
    b=int(input('Insira outro número MENOR:'))
c=a
print(a)
while c!=b:
    c=c-1  
    print(c)