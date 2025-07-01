"""
ORDENAMIENTO BURBUJA: Implementación del algoritmo clásico de ordenamiento.
Conceptos clave:
- Algoritmo O(n²) (complejidad cuadrática)
- Operaciones in-place (modifica lista original)
- Comparación e intercambio de elementos adyacentes.
"""

import random

def bubble_sort(list):
    length = len(list)
    for i in range(length):  # O(n) pasadas
        for j in range(0, length - i - 1):  # O(n) comparaciones
            if list[j] > list[j+1]:
                # Intercambio de elementos
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(f"Lista original: {list}")

    sorted_list = bubble_sort(list.copy())  # Usamos copy() para no modificar la original
    print(f"Lista ordenada: {sorted_list}")

