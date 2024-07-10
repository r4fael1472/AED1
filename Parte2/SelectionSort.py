import time
from time import sleep

def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(f"{i+1} rodada:")
        sleep(3)
        print(seq)
        indiceMenor = i
        for j in range(i+1, n):
            if seq[j] < seq[indiceMenor]:
                indiceMenor = j #salva o índice do menor
        if indiceMenor != i:
            temp = seq[i]
            seq[i] = seq[indiceMenor]
            seq[indiceMenor] = temp
    print("Sequencia Ordenada: ")
    return seq



sequencia = [3,5,2,1,6]

print(selection_sort(sequencia))
