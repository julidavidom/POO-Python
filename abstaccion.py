"""
ABSTRACCIÓN: Modela una lavadora ocultando detalles internos.
POO aplicado:
- Abstracción (simplifica la realidad)
- Encapsulamiento (métodos privados __)
- Interfaz pública (método 'lavar')
"""

class WashingMachine:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self.__fill_water_tank(temperature)
        self.__add_soap()
        self.__wash_clothes()
        self.__spin()

    def __fill_water_tank(self, water_temperature):
        print(f'Filling tank with {water_temperature} water')

    def __add_soap(self):
        print(f'Adding soap')

    def __wash_clothes(self):
        print(f'Washing clothes')

    def __spin(self):
        print(f'Spinning')


if __name__ == "__main__":
    washer = WashingMachine()
    washer.wash()





