'''
Programa para entender el polimorfismo.
'''
class Persona() :
    def __init__(self, nombre):
        self.nombre=nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista( Persona): #  Clase ciclista extiende clase persona
    def __init__(self,nombre): # tenemos un referencia a la super clase
        super().__init__(nombre)

    def avanza (self): 
        print ('Ando moviendome en mi bicicleta ') #aca lafuncion avanza es diferente a la de la calse perosona, esto es la ventaja del polimorfismo


def main():
    persona=Persona('David')
    persona.avanza()
    ciclista = Ciclista('Daniel')
    ciclista.avanza()

    

if __name__ == "__main__":
    main()