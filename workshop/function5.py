def primeiro_exercicio(n1):
    s = n1 + 1
    a = n1 - 1
    return (f"seu sucessor é {s} e seu antecessor é {a}")
#segundo exercicio
def segundo_exercicio(n1, n2):
    soma = n1 + n2 
    mult = n1 * n2 
    div = n1 / n2 
    return (f"{n1} + {n2} = {soma}   {n1} * {n2} = {mult}   {n1} / {n2} = {div}")
#teceiro exercicio
def terceiro_exercicio(n1, n2):
    if n1 > n2:
        valor = "True"
    else:
        valor = "False"
        return valor
#quarto exercicio 
def quarto_exercicio(c):
    f = (c * 1.8) + 32
    return f
def quinto_exercicio(idade):
    if idade >= 18:
        apto = "Pode dirigir"
    else:
        apto = "não pode dirigir"
        return apto
def sexto_exercicio(velocidade):
    limite = 80
    multa = 7
    if velocidade > limite:
        passou = (velocidade - limite) * 7
        return passou
