"""
ORDENAMIENTO POR MEZCLA: Implementación del algoritmo Merge Sort recursivo.
Conceptos clave:
- Algoritmo O(n log n) (divide y vencerás)
- Recursividad (llamadas a sí mismo)
- Fusión (merge) de sublistas ordenadas

"""

import random

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left, '*'*8, right)

        # Llamadas recursivas
        merge_sort(left)
        merge_sort(right)

        # Fusionar las sublistas
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]  # Corregido error (antes era derecha[i])
                j += 1
            k += 1

        # Elementos restantes de izquierda
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        # Elementos restantes de derecha
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print(f'Left {left}     Right {right}')
        print(list)
        print('*' * 40)

    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print("Lista original:", list)
    print('-' * 20)

    sorted_list = merge_sort(list.copy())
    print("Lista ordenada:", sorted_list)