import random

def busqueda_lineal (lista, objetivo):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match= True
            break # el brak no cambia la complejidad algoritmica, solo en promedio nos tardamos menos.
    return match  

if __name__ == "__main__":
    tamano_de_lista=int(input('De que tamaño sera la lista ?'))
    objetivo = int(input('Que numero quieres encontar? '))
    lista=[random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    encontrado=busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo}{" esta" if encontrado else "no esta"} en la lista' )