'''
Cuales son los elementos que caben en mi mochila que me otorgan el
mayor valor posible. 
 
Como no podemos subdividr nuestros elementos necesitamos escoger o no escer un archivo.
'''

def morral (tamaño_morral, pesos, valores, n ): #n es el indice que vamos a estar trabajando
    if n == 0 or tamaño_morral==0: # si y no tenemos mas elementos, o si e tamaño del morra es 0(lleno).
        return 0

    if pesos[n-1] > tamaño_morral: # si  el elemento que quiero meter al morral pesa mas que el tamaño que me queda del morral 
        return morral(tamaño_morral, pesos , valores, n-1) # funcion recursiva que toma el valor
    #puedo tomar o no tomar el elemento. SI yo tomo un valor ¿que valor tendria?  comparandolo con otro 
    return max(valores[n-1] + morral(tamaño_morral - pesos[n-1], pesos,valores, n-1 ), morral(tamaño_morral,pesos,valores,n-1)) # si si tengo espacio para el elemento, escoge el valor mas alto


if __name__ == "__main__":
    valores=[60, 100,120]s
    pesos=[10,20,30]
    tamaño_morral= 50
    n = len (valores)
    resultado = morral(tamaño_morral, pesos, valores, n)
    print(resultado)
