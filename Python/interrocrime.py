# Progrma que faz 5 perguntas e avalia o nivel de suspeito da pessoa.

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "já trabalhou para a vítima? "
]

def interrogar():
    c=0
    print("Responda com sim ou não para as cinco perguntas a seguir, para verificarmos o quão suspeito você é!")
    for i in perguntas:
        p = input(i)
        if p.lower() == "sim":
            c = c+1
    if c == 2:
        print("Você é suspeito!")
    elif 2<c<5:
        print("Você é cúmplice!") 
    elif c==5:
        print("Você é o ASSASSINO! PRENDAM ELE!")
    else:
        print("Você com certeza é inocente!")

interrogar()