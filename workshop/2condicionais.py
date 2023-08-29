#quinto exercicio
idade = int(input())
if idade >= 18:
    print("pode digirir")
else:
    print("não pode dirigir")
#sexto exercicio 
velocidade = int(input())
limite = 80
multa = 7
if velocidade > limite:
    passou = (velocidade - limite) * 7
    
    print(f"você irar pagar {passou}R$")
else: 
    print("Você não foi multado")
#setimo exercicio 
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n3:
    print("o primeiro numero e o maior")
elif n2 > n1 and n3:
    print("o segundo numero e o maior")
elif n3 > n1 and n2:
    print("o segundo numero e o maior")
else:
    print("todos são iguais")
#oitavo exercicio
caneta_preta = float(input())
caneta_azul = float(input())

valor_preta = caneta_preta * 2.5
valor_azul = caneta_azul * 2.0
valor_final = valor_preta + valor_azul
print(valor_final)
#nono exercicio 
nome1 = input()
nomes = ["joao maia",  "joao abrantes", "pedro"]
if nome1 == nomes[0,1,2]:
    print(f"ola ,eu nome é {nomes} ")