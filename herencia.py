class Rectangulo:

    def __init__(self , base , altura):
        self.base= base
        self.altura= altura

    def area(self):
        return self.base * self.altura


class Cuadrado (Rectangulo): # La clase cuadrado extiende a la calse rectangulo , heredamos el comportamieno, Rectanglo es la super clase. 
    def __init__(self, lado):
        super().__init__(lado,lado)#super nos permite optener  una referenca directa de la super clase Rectagunlo

 
if __name__ == "__main__":
    rectangulo = Rectangulo(base=3, altura=4)
    print (rectangulo.area())

    cuadrado= Cuadrado(lado=5)
    print(cuadrado.area())    #Estamos utilizando el metodo area  dentro de nuestra calse cuadrado, aunque no lo emos definido, es decir, estamos heredando un metodo.