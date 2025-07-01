"""
CASILLA DE VOTACIÓN: Demostración del uso de properties para validación de atributos.
POO aplicado:
- Encapsulamiento (atributos protegidos con _)
- Properties (getter/setter con validación)
- Validación de datos (región debe pertenecer al país)
"""

class VotingBooth:

    def __init__(self, id, country):
        self._id = id
        self._country = country
        self._region = None

    @property
    def region(self):
        """Getter para la región (fget)"""
        return self._region

    @region.setter
    def region(self, region):
        """Setter con validación (fset)
        Raises:
            ValueError: Si la región no existe en el país
        """
        if region in self._country:
            self._region = region
        else:
            raise ValueError(f'La región {region} no es válida en {self._country}')

if __name__ == "__main__":
    # Prueba de funcionamiento
    booth = VotingBooth(123, ['Ciudad de México', 'Morelos'])
    print(f"Región inicial: {booth._region}")

    # Asignación válida
    booth.region = 'Ciudad de México'
    print(f"Región asignada: {booth.region}")

    # Intento de asignación inválida
    try:
        booth.region = 'Jalisco'
    except ValueError as e:
        print(f"Error: {e}")

