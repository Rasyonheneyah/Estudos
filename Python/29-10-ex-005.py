

"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero
e os demais atributos são obrigatórios
"""

class contaCorrente:

    def __init__(self, numConta, correntista):
        self.numConta = numConta
        self.correntista = correntista
        self.saldo = 0
    
    def alterarNome():