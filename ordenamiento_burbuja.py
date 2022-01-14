import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range (n) : #este proceso tiene una complejidad algoritmica de O(n^2)
        for j in range (0, n - i - 1): # empezamos en 0, n - i para no tener en cuenta lo que ya recorrimos, -1 poeque trabajaremos con indices de un Len
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1]=lista[j+1],lista[j]
    return (lista)
    
if __name__ == "__main__":
    tamaño_lista=int(input('Ingrese el tamaño de la lista: '))
    lista=[random.randint(0,100) for i in range(tamaño_lista)]
    print(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

