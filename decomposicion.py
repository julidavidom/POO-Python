"""
MODELADO DE AUTOMÓVIL: Demostración de composición de clases para modelar sistemas complejos.

POO aplicado:
- Composición (Automovil contiene un Motor)
- Encapsulamiento (variables privadas _estado, _motor, _temperatura)
- Delegación de comportamiento (acelerar delega al motor) 
"""

class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'stopped'  # Variable privada
        self._engine = Engine(cylinders=4)  # Composición
    
    def accelerate(self, mode='slow'):
        if mode == 'fast':
            self._engine.inject_gasoline(10)
        else:
            self._engine.inject_gasoline(3)
        self._status = 'moving'

class Engine:
    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0
    
    def inject_gasoline(self, amount):
        """Simula inyección de combustible"""
        self._temperature += amount * 2  # Aumento simulado de temperatura