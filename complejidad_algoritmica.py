"""
CÁLCULO DE FACTORIAL: Comparación de implementación iterativa vs recursiva.
Conceptos clave:
- Recursividad (función que se llama a sí misma)
- Iteración (bucle while)
- Análisis de rendimiento (complejidad O(n) en ambos casos)
"""

import time
import sys

def factorial_iterative(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

def recursive_factorial(number):
    if number == 1:
        return 1
    return number * recursive_factorial(number - 1)

if __name__ == "__main__":
    sys.setrecursionlimit(100000)  # Aumentamos el límite de recursión

    number = 10000  # Número para calcular factorial

    # Medición tiempo versión iterativa
    start_time = time.time()
    factorial_iterative(number)
    end_time = time.time()
    print(f"Tiempo iterativo: {end_time - start_time} segundos")

    # Medición tiempo versión recursiva
    start_time = time.time()
    recursive_factorial(number)
    end_time = time.time()
    print(f"Tiempo recursivo: {end_time - start_time} segundos")


