from BuscaLinearOuSequencial import busca_linear

def busca_binaria(lista, alvo):
    ini = 0
    fim = len(lista) - 1
    contador = 0
    while ini <= fim:
        contador += 1
        meio = (ini + fim) // 2
        if lista[meio] == alvo:
            return f"O valor escolhida está na lista e o while rodou {contador} vezes."
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            ini = meio + 1
    return "O valor escolhido não está na lista."

# a lista precisa estar ordenada
lista = [3,4,6,9,12,14,21,36,38]

alvo = int(input("Digite o valor desejado:"))
print(busca_binaria(lista, alvo))
print(busca_linear(lista, alvo))


