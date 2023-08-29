#decimo exercicio 
for i in range(0,11):
    print(i)
#decimo primeiro
for i in range(10,-1,-1):
    print(i)
#decimo segundo
for i in range(0,12,2):
    print(i)
#decimo teceiro
n1 = int(input())
for i in range(0,10):
    soma = n1 + i
    print(f"a soma de {n1} + {i} é igual {soma}")
#decimo quarto
nome = input()
while nome != "parar":
    nome = input("digite outro nome")
#decimo quinto
while True:
    n1 = int(input())
    if n1 == 0:
        break
#decimo sexto
nome = input()
while nome == "M" or "F":
    nome = input()
    if nome == "sair":
        break