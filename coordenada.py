"""
CÁLCULO DE DISTANCIA ENTRE COORDENADAS: Implementación de clase para representar puntos y calcular distancias.
POO aplicado:
- Encapsulamiento (datos y métodos en una clase)
- Métodos de instancia (distancia)
- Constructor (__init__)
"""

class Coordinate:

    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def distance(self, other_coord):  # Calcula distancia euclidiana
        x_diff = (self.x - other_coord.x)**2
        y_diff = (self.y - other_coord.y)**2
        return (x_diff + y_diff)**0.5  # Teorema de Pitágoras

if __name__ == "__main__":
    coord1 = Coordinate(3, 30)  # Instancia 1
    coord2 = Coordinate(4, 8)   # Instancia 2

    # Demostración de funcionalidad
    print(f"Distancia entre coordenadas: {coord1.distance(coord2):.2f}")
    print(f"¿coord2 es instancia de Coordinate?: {isinstance(coord2, Coordinate)}")