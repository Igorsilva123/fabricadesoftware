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

class Banco():
    def __init__(self, titular, saldos, sacar, depositar):
        self.titular = titular
        self.saldos = saldos
        def sacar(self, dinheiro):
            self = dinheiro 

        self.depositar = depositar


