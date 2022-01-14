'''
La fucion interna de python property determina cuatro atributos, 
            fget : trae el valor de un atributo.
            fset : define el valor de un atributo.
            fdel : elimina el valor de un atributo.
            fdoc : crea un docstring por atributo.

'''

class Casilladevotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

        @property                      #TRAE EL VALOR DEL ATRIBUTO REGION
        def region(self):
            return self._region

        @region.setter
        def region(self, region):      #DEFINE  El VALOR DE EL ATRIBUTO REGION
            if region in self._pais:
                self._region=region
            raise ValueError(f'La region {region} no es valida en {self._pais}')

if __name__ == "__main__":
    casilla = Casilladevotacion(123,['Ciudad de mexico', 'Morelos'])
    print(casilla._region)
    casilla.region='Ciudad de mexico'
    print(casilla.region)

