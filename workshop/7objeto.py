class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome 
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        return f'oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}'
    
pedro = Pessoa('Pedro', 25, 'reporter')
pedro.saudacao()

guilherme = Pessoa("Guilherme", 18, 'estudante')
guilherme.saudacao

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, op):
        saldo_final = int(self.saldo) + int(op)
        print (f'Olá {self.titular}, você depositou. Seu saldo é de {saldo_final}')

    def sacar(self, op):
        saldo_final = int(self.saldo) - int(op)
        print (f'Olá {self.titular}, você sacou. Seu saldo é de {saldo_final}')
    
    
banco = ContaBancaria('Igor', 1000)
banco.depositar("500")

    
banco = ContaBancaria('Igor', 1000)
banco.sacar("1000")


