'''
Gernerar el factorial  de un numero.

Generaremos a implementacion iterativa y una recursiva
 Asi compararemos las dos implementaciones.

'''

import time
import sys


def factorial(n):
    respuesta=1
    while n > 1:
        respuesta = respuesta*n
        n=n-1
    return respuesta
   

def factorial_recursivo(n):
    if n == 1 : 
        return 1
    return n*factorial_recursivo(n-1)
    
    

if __name__ == "__main__":
    sys.setrecursionlimit(100000) #definimos un valor mayor de recursibidad
    n = 10000

    comienzo1= time.time()
    factorial(n)
    final2 = time.time()
    print(final-comienzo)

    comienzo= time.time()
    factorial_recursivo(n)
    final= time.time()
    print(final-comienzo)


