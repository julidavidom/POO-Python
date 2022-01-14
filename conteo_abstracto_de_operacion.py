'''
Tomar el tiempo es rasonable para medir un algoritmo, pero hay muchosfactores que no se 
controlan. 

Para hacer una aproximacion mas sercana de como va a crecer nuestra funcion.

Queremos contar que esta pasando dentro de nuestro programa.
'''

def f(x):
    respuesta = 0   #aca esta nuestro primer paso '''
    for i in range (1000): #no depende de x, esto correra 1000 veces'''
        respuesta += 1
    for i in range (x): #si depende de x''' 
        respuesta += x
    for i in range (x): 
        for j in range (x): #cuado hay un for dentro de otro quiere decir que el primer bucle empiza el el primer dato de i , posterioreme recorre todos los datos de j,  y realiza la misma operacion desde el segundo dato de i'''
            respuesta += 1
            respuesta += 1  # estamos generando 2 operaciones, y estamos recoriendo dos veces x.
        return respuesta

'''
Podemos representar esto en una ecuacion

F(X)=1002 + x + 2x^2

Podemos inferir  que los procesos que mas estan generando 
proceso es el bucle for doble, que representa 2x^2.

para olvidarnos de los terminos que no importan utilizaremos e metodo Big O notacion
'''
