"""
BÚSQUEDA BINARIA: Algoritmo de búsqueda eficiente en listas ordenadas.
POO aplicado:
- Recursividad (función que se llama a sí misma)
- Divide y vencerás (divide el problema en subproblemas)
"""

import random

def binary_search(sorted_list, start, end, target):
    print(f'Searching {target} between {sorted_list[start]} and {sorted_list[end-1]}')
    if start > end:
        return False
    mid = (start + end) // 2
    if sorted_list[mid] == target:
        return True
    elif sorted_list[mid] < target:
        return binary_search(sorted_list, mid+1, end, target)
    else:
        return binary_search(sorted_list, start, mid-1, target)

if __name__ == "__main__":
    list_size = int(input('What size should the list be? '))
    target = int(input('What number to find? '))
    sorted_list = sorted([random.randint(0,100) for _ in range(list_size)])
    print(sorted_list)
    found = binary_search(sorted_list, 0, len(sorted_list), target)
    print(f'Element {target} {"is" if found else "is not"} in the list')