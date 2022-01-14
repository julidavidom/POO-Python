class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self.__llenar_tanque_de_agua(temperatura)
        self.__añadir_jabon()
        self.__lavar()
        self.__centrifugar()

    def __llenar_tanque_de_agua (self, temperatura_agua):
        print(f'Llenando el tanque con agua {temperatura_agua}')
    def __añadir_jabon(self):
        print(f'Añadiendo jabon')
    def __lavar (self):
        print(f'Lavando')
    def __centrifugar(self):
        print(f'Centrifugando')
        
 

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()





