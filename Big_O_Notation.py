"""
ANÁLISIS DE COMPLEJIDAD ALGORITMICA (Big O Notation)

Ejemplo 1: O(n) - Complejidad lineal
- Dos bucles simples O(n) + O(n) = O(2n) → Simplificado a O(n)
- Crecimiento proporcional al tamaño de entrada

Ejemplo 2: O(n²) - Complejidad cuadrática
- Bucle simple O(n) + bucle anidado O(n²) → O(n + n²) → O(n²)
- Termino dominante n²

Ejemplo 3: O(n²) - Complejidad cuadrática
- Bucle anidado O(n)*O(n) = O(n²)
- Crecimiento proporcional al cuadrado de la entrada

Ejemplo 4: O(2^n) - Complejidad exponencial
- Función recursiva con múltiples llamadas (Fibonacci)
- Crecimiento exponencial (árbol de recursión binario)

Traducciones:
f → function (aunque se mantiene como ejemplo)
n → size (parámetro de tamaño)
m → secondary_size (parámetro secundario)
o → zero (error tipográfico corregido)
"""

# Ejemplo 1: O(n)
def example_linear(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)

# Ejemplo 2: O(n²)
def example_quadratic(n, m):
    for i in range(m):
        print(i)
    for i in range(n*n):
        print(i)

# Ejemplo 3: O(n²)
def example_nested_loops(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# Ejemplo 4: O(2^n)
def fibonacci(n):
    if n == 0 or n == 1:  # Corregido error tipográfico (o → 0)
        return n
    return fibonacci(n-1) + fibonacci(n-2)
