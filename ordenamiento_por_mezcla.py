import random
def ordenamiento_por_mezcla (lista):

    if len(lista) > 1:

        medio= len(lista)//2
        izquierda=lista[:medio]
        derecha=lista[medio:]
        print(izquierda,'*'*8, derecha )

        #llamada recursiva en cada mitad (se ejecuta hassta que tengamos lista de 1 solo tamaño)
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        #iteradores para recorrer las sublistas
        i=0
        j=0
        #iterador para la lista principal
        k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k]=derecha[i]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k]=izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k]=derecha[j]
            j  += 1
            k += 1

        print(f'Izquierda   {izquierda}     Derecha  {derecha}')
        print(lista)
        print('*'*40)

    return lista 
    
if __name__ == "__main__":
    tamano_lista=int(input('Ingrese el tamaño de la lista: '))
    lista=[random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-'*20)
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)