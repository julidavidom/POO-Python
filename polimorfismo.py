"""
POLIMORFISMO: Demostración de cómo objetos de diferentes clases responden al mismo mensaje.
POO aplicado:
- Herencia (Ciclista hereda de Persona)
- Polimorfismo (mismo método, comportamientos diferentes)
- Sobreescritura de métodos (override)
"""

class Person:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} está caminando')

class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)  # Llama al constructor de Person

    def move(self):  # Sobreescribe el método de Person
        print(f'{self.name} está moviéndose en bicicleta')

def main():
    # Demostración de polimorfismo
    person = Person('David')
    person.move()  # Output: Está caminando

    cyclist = Cyclist('Daniel')
    cyclist.move()  # Output: Está en bicicleta

    # Polimorfismo en acción
    for character in [person, cyclist]:
        character.move()  # Mismo método, comportamientos diferentes

if __name__ == "__main__":
    main()