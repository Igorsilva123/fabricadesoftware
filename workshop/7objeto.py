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

class FormaGeometrica:
    def calcular_area(self, raio):
        return 3.14*(raio**2)
class Circulo(FormaGeometrica):
    pass
class Retangulo(FormaGeometrica):
    def calcular_area(self, base, altura):
        return base * altura

circulo = Circulo()
area = circulo.calcular_area(20)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_area(5,10)
print(area)


class Animal:
    def barulho(self):
        pass 

class Cachorro(Animal):
    def barulho(self):
        return "auuuu"
    
class Gato(Animal):
    def barulho(self):
       return "miaaauu"

def animal_barulho(animal):
    print(animal.barulho())

cachorro = Cachorro()
gato = Gato()


animal_barulho(cachorro)
animal_barulho(gato)



