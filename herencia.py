"""
HERENCIA GEOMÉTRICA: Demostración de herencia en POO donde Cuadrado hereda de Rectángulo.
POO aplicado:

- Herencia (Cuadrado es subclase de Rectangulo)
- Reutilización de código (método area heredado)
- Llamado a superclase (super().__init__)

"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calcula área del rectángulo"""
        return self.width * self.height


class Square(Rectangle):  # Square hereda de Rectangle
    def __init__(self, side):
        super().__init__(side, side)  # Llama al constructor de Rectangle

if __name__ == "__main__":
    # Demostración con rectángulo
    rectangle = Rectangle(width=3, height=4)
    print(f"Área del rectángulo: {rectangle.area()}")

    # Demostración con cuadrado (usa herencia)
    square = Square(side=5)
    print(f"Área del cuadrado: {square.area()}")  # Método heredado