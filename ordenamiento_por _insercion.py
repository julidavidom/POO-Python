"""
ORDENAMIENTO POR INSERCIÓN: Implementación del algoritmo de inserción con impresión de pasos.
Conceptos clave:
- Algoritmo O(n²) (complejidad cuadrática)
- Ordenamiento in-place (modifica lista original)
- Eficiente para listas pequeñas o casi ordenadas

"""

import random

def insertion_sort(list):
    for index in range(1, len(list)):  # Comenzamos desde 1 (corrección)
        current_value = list[index]
        current_position = index
        print(f"Valor actual: {current_value}, Posición: {current_position}")

        # Mover elementos mayores hacia la derecha
        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1
            list[current_position] = current_value
            print(f"Paso intermedio: {list}")

    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(f"Lista original: {list}")

    sorted_list = insertion_sort(list.copy())  # Usamos copy() para no modificar la original
    print(f"Lista ordenada: {sorted_list}")