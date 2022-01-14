'''
Este programa determina la distancia entre dos cordenadas
'''

class Coordenada:

    def __init__ (self, x,y): #ESTE ES MI CONSTRUCTOR.
        self.x=x
        self.y=y
    
    def distancia(self, otra_cantidad): #Otra coordenada es nuestar instancia
        x_diff = (self.x - otra_cantidad.x)**2
        y_diff = (self.y - otra_cantidad.y)**2
        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3,30)  #Definimos una iantancia de la coordenada 1
    coord_2=Coordenada(4, 8)  #Definimos una instancia de la coordenada 2
    print(coord_1.distancia(coord_2)) #Podemo ejecutar los metodos creadados especificos de cada clase
    print(isinstance(coord_2, Coordenada)) # Podemos preguntar si coord_2 es intancia de la clase coordenada