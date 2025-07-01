"""
PROBLEMA DE LA MOCHILA (0/1): Solución recursiva para maximizar valor sin exceder capacidad.
Conceptos clave:
- Programación dinámica (memoization implícita)
- Recursividad (llamadas anidadas)
- Decisión binaria (tomar o no tomar cada elemento)
"""

def knapsack(capacity, weights, values, current_index):
    # Caso base: no hay elementos o no queda espacio
    if current_index == 0 or capacity == 0:
        return 0

    # Si el peso del elemento actual excede la capacidad disponible
    if weights[current_index-1] > capacity:
        return knapsack(capacity, weights, values, current_index-1)

    # Maximizar entre:
    # 1. Tomar el elemento actual + mejor solución del resto
    # 2. No tomar el elemento actual
    return max(
        values[current_index-1] + knapsack(capacity-weights[current_index-1], weights, values, current_index-1),
        knapsack(capacity, weights, values, current_index-1)
    )

if __name__ == "__main__":
    values = [60, 100, 120]  # Valores de los items
    weights = [10, 20, 30]   # Pesos de los items
    capacity = 50            # Capacidad máxima de la mochila
    n = len(values)          # Cantidad total de items

    max_value = knapsack(capacity, weights, values, n)
    print(f"El valor máximo obtenible es: {max_value}")