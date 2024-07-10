def busca_linear(lista, alvo):
    contador = 0
    for item in lista:
        contador += 1
        if item == alvo:
            return f"O valor está na lista e o for rodou {contador} vezes."
    return "O valor não está na lista"

