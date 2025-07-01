"""
ANÁLISIS DE COMPLEJIDAD: Contando operaciones para determinar crecimiento de función.
Conceptos clave:
- Conteo de operaciones básicas
- Identificación de términos dominantes
- Big O notation (simplificación de complejidad)

Ecuación de operaciones:

    f(n) = 1000 + n + 2n²

El bucle anidado domina el crecimiento para valores grandes de n.
"""

def count_operations(input_size):
    total_operations = 0  # 1 operación inicial

    # Bucle independiente del input (1000 operaciones)
    for _ in range(1000):
        total_operations += 1

    # Bucle lineal O(n)
    for _ in range(input_size):
        total_operations += 1

    # Bucle anidado cuadrático O(n²)
    for _ in range(input_size):
        for __ in range(input_size):
            total_operations += 1  # 1ra operación
            total_operations += 1  # 2da operación

    return total_operations

