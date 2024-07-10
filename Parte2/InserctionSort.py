
def inserction_sort(seq):
    n = len(seq)
    for i in range(1, n):
        print(seq)
        valor = seq[i]
        pos = i
        while pos > 0 and valor < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = valor
    return seq


sequencia = [5, 3, 2, 1, 6]


print(inserction_sort(sequencia))

