def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        print(array)
        for j in range(n-1-i):
            menor = array[j]
            if array[j+1] < menor:
                temp = array[j+1]
                array[j+1] = menor
                array[j] = temp
    return array

lista = [5, 12, 4, 2, 91, 30]

print(bubble_sort(lista))