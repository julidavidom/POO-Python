"""
BÚSQUEDA LINEAL: Algoritmo de búsqueda que recorre secuencialmente una lista.
Conceptos clave:
- Complejidad O(n) (lineal) - Peor caso recorre toda la lista
- Uso de break para optimización (no afecta complejidad en peor caso)
"""
import random

def linear_search(list, target):
    found = False
    for element in list:
        if element == target:
            found = True
            break  # Optimización que no cambia la complejidad O(n)
    return found

if __name__ == "__main__":
    list_size = int(input('¿De qué tamaño será la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(list)
    is_found = linear_search(list, target)
    print(f'El elemento {target} {"está" if is_found else "no está"} en la lista')