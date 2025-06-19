# Programación Orientada a Objetos (POO)
Uno de los elementos más importantes de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos. La clave para entender la programación orientada a objetos es pensar en objetos como agrupaciones de datos y que metodos se usaran para que se operan dichos datos. 

Podemos representar a una persona con propiedades como nombre, edad, género,etc, y los comportamientos de dicha persona como caminar, cantar, comer, etc.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def caminar(self):
        print(f"{self.nombre} está caminando")
```

De la misma manera podemos representar unos audífonos con propiedades como su marca, tamaño, color, etc. y sus comportamientos como reproducir música, pausar y avanzar a la siguiente canción.

```python
class Audifonos:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def reproducir(self):
        print("Reproduciendo música...")
```

Puesto de otra manera, la programación orientada a objetos nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos.

- **Objetos**: Agrupaciones de datos (atributos) y métodos que operan sobre esos datos.
- **Clases**: Plantillas para crear objetos, definiendo estructura y comportamiento.

Hasta ahora, en las publicaciones y blogs anteriores  hemos utilizado programación orientada a objetos de manera implícita. Hemos utilizado los tipos lista y diccionario, entre muchos otros, así como los métodos asociados a dichos tipos. Los creadores de un lenguaje de programación sólo pueden diseñar una fracción muy pequeña de todas las funciones útiles (como abs, float, type, etc.), también pueden escribir una fracción muy pequeña de los tipos útiles (int, str, dict, list, etc.). Ya sabemos los mecanismos que nos permiten crear funciones, ahora veremos los mecanismos que nos permiten crear nuevos tipos o clases.

## Historia y Evolución (Contexto Académico)
La POO tiene sus raíces en varios hitos importantes:

- **1967:** Simula 67, primer lenguaje con características de POO.
- **1972:** Smalltalk desarrollado en Xerox PARC (Alan Kay).
- **1983:** C++ como extensión de C con POO (Bjarne Stroustrup).
- **1995:** Java populariza la POO en entornos empresariales. 

Según un estudio de IEEE de 2020, el 86% de los lenguajes modernos soportan POO como paradigma principal, demostrando su relevancia actual.

## Clases en Python
Las estructuras primitivas con las que hemos trabajado hasta ahora nos permiten definir cosas sencillas, como el costo de algo, el nombre de un usuario, las veces que debe correr un bucle, etc. Sin embargo, existen ocasiones cuando necesitamos definir estructuras más complejas, por ejemplo un hotel. Podríamos utilizar dos listas: una para definir los cuartos y una segunda para definir si el cuarto se encuentra ocupado o no.Este tipo de organización rápidamente se sale de control. ¿Qué tal que quisieramos añadir más propiedades, cómo si el cuarto ya fue aseado o no? ¿Si el cuarto tiene cama doble o sencilla?. Esto nos lleva a una falta fuerte de organización y es justamente el punto que justifica la existencia de clases.

### Ejemplo hotel sin Clases
```python
cuartos_de_hotel = [101, 102, 103]
cuarto_ocupado = [True, False, False]
cuarto_aseado = [False, True, True]
```
Las clases nos permiten crear nuevos tipos que contienen información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases Hotel() y Cuarto() que nos permitiera dar seguimiento a las propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.

### Ejemplo Hotel con Clases
```python
class Habitacion:
    def __init__(self, numero, ocupada=False, aseada=True):
        self.numero = numero
        self.ocupada = ocupada
        self.aseada = aseada

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, numero):
        self.habitaciones.append(Habitacion(numero))
```
Es importante resaltar que las clases sólo proveen estructura. Son un molde con el cual podemos construir objetos específicos. La clase señala las propiedades que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para eso necesitamos las instancias.

## Instancias
Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos en nuestro programa: un hotel llamado PlatziHotel o Hilton. Otra forma de pensarlo es que las clases son como un formulario y una vez que se llena cada copia del formulario tenemos las instancias que pertenecen a dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia es distinta de las demás (aunque todas pertenecen a una misma clase).

Para definir una clase, simplemente utilizamos el keyword class.

```python  
    class Hotel:
        pass
```
Una vez que tenemos una clase llamada Hotel podemos generar una instancia llamando al constructor de la clase.
 
```python  
 hotel = Hotel()
```
### Atributos de la instancia:

Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos el método especial ¨**__init__** para definir el estado inicial de nuestra instancia. 
Recibe como primer parámetro obligatorio self (que es simplemente una referencia a la instancia).

```python
class Hotel:
    def __init__(self, capacidad, estacionamientos):
        self.capacidad_maxima = capacidad
        self.estacionamientos = estacionamientos
        self.huespedes = 0

hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
```

## Métodos de Instancia
Mientras que los atributos de la instancia describen lo que representa el objeto, los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y normalmente operan en los mencionados atributos. Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben self como primer argumento.

```python
class Hotel:
    # ... __init__ anterior
    
    def anadir_huespedes(self, cantidad):
        """Añade huéspedes al hotel con validación de capacidad"""
        if self.huespedes + cantidad > self.capacidad_maxima:
            raise ValueError("Excede capacidad máxima")
        self.huespedes += cantidad
    
    def checkout(self, cantidad):
        """Retira huéspedes del hotel"""
        self.huespedes = max(0, self.huespedes - cantidad)
    
    def ocupacion_actual(self):
        """Devuelve la ocupación actual"""
        return self.huespedes

hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
print(f"Ocupación: {hotel.ocupacion_actual()}")  # 3
```

## Tipos de Datos Abstractos
En Python, todo elemento es un objeto que pertenece a un tipo específico. Estos objetos permiten tres interacciones fundamentales:

- Creación: Construcción del objeto mediante su inicialización.
- Manipulación: Operaciones que modifican su estado interno.
- Destrucción: Liberación de recursos (automática en Python).

**Ventajas clave**
- Descomposición: Dividir sistemas complejos en componentes manejables.
- Abstracción: Enfocarse en características esenciales ignorando detalles técnicos.
- Encapsulación: Proteger datos internos exponiendo solo interfaces controladas.

## Descomposición: Estrategia de Diseño
Técnica para resolver problemas complejos mediante:

1. División modular: Crear componentes especializados
2. Jerarquías lógicas: Organizar responsabilidades entre clases
3. Acoplamiento mínimo: Reducir dependencias entre partes

**Resultado:** Código mantenible y escalable donde cada clase gestiona una funcionalidad específica

### Un ejemplo sencillo donde se aplica la descomposición

```python
class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'stopped'  # Variable privada
        self._engine = Engine(cylinders=4)  # Composición

    def accelerate(self, mode='slow'):
        if mode == 'fast':
            self._engine.inject_gasoline(10)
        else:
            self._engine.inject_gasoline(3)
        self._status = 'moving'

class Engine:
    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, amount):
        """Simula inyección de combustible"""
        self._temperature += amount * 2  # Aumento simulado de temperatura
```

## Abstracción: Simplificación Efectiva
Principio que permite:

- Enfoque selectivo: Priorizar información relevante para el contexto.
- Ocultamiento técnico: Esconder detalles de implementación complejos.
- Interfaces claras: Exponer métodos públicos para interacción controlada.


### Un ejemplo sencillo donde se aplica la abstracción 
```python
class WashingMachine:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self.__fill_water_tank(temperature)
        self.__add_soap()
        self.__wash_clothes()
        self.__spin()

    def __fill_water_tank(self, water_temperature):
        print(f'Filling tank with {water_temperature} water')

    def __add_soap(self):
        print(f'Adding soap')

    def __wash_clothes(self):
        print(f'Washing clothes')

    def __spin(self):
        print(f'Spinning')

if __name__ == "__main__":
    washer = WashingMachine()
    washer.wash()
```
## Analisando un poco de lo anterior 
- Mientras que la clase es un molde, los objetos creados se les conoce como iantancias.
- Cuando se crea una instancia, se ejecuta el metodo __init__
- Todos los metodos de una clase reciben implicitamente como primer parameto self
- Los atributos de clase nos permiten
    - Representar datos
    - Procedimientos para interactuar con los metodos.
    - Mecanismos para esconder la representacion interna
- Se accede a los atributos con la notacion de punto .
- Puede tener atributos privados. Por convencion comiensan con _

## FUNCIONES: BASES DE LOS DECORADORES
Los decoradores son una forma sencilla de llamar funciones de orden mayor, es decir, funciones que toman otra función cómo parámetro y/o retornan otra función como resultado. De esta forma un decorador añade  capacidades a una función sin modificarla.

Un ejemplo de esto son las llantas de un automóvil si les colocas cadenas para la nieve: aún puede andar y además extiende su funcionalidad para conducirse en otros terrenos.

## Funciones cómo objetos de primera-clase
Otro concepto importante a tener en cuenta es que en Python las funciones son objetos de primera-clase, es decir  que pueden ser pasados y utilizados cómo argumentos al igual que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).

Un ejemplo donde se definen 3 diferentes funciones que trabajan de manera conjunta

```python
def presentarse(nombre):
    return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
    return funcion_entrante("David")
```
Las primeras dos funciones son obvias en su resultado, donde se mostrarán un mensaje con el valor de la variable nombre. La tercer función puede ser más compleja de predecir ya que toma una función cómo entrada,  veamos que pasa cuando colocamos una función cómo atributo.

```
consume_funciones(presentarse)
'Me llamo David'

consume_funciones(estudiemos_juntos)
'¡Hey David, aprendamos Python!'
```
Asi, la función consume_funciones() se ejecuta, mientras que la función presentarse y estudiemos_juntos son solo para hacer referencia.

## Funciones anidadas
Al igual que los condicionales y bucles también puedes colocar funciones dentro de otra función.
Toma un minuto para analizar el siguiente código.

```python
def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash y Flask.")
```
                
Si llamamos a la función funcion_mayor tendremos la siguiente salida:

```
funcion_mayor()
Esta es una función mayor y su mensaje de salida.
Algunos frameworks de Python son: Django, Dash y Flask.
Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.
```

Debemos considerar que las funciones anidadas dentro de funcion_mayor no se ejecutan sino hasta que se llama esta primera, siendo muestra del scope o alcance de las funciones y si las llamamos obtendremos un error.

## Setters, getters y decorador property

```python
def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)" 
    return wrapper

def zumbido():
    print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)
```

¿Qué pasará si se  llama a la función zumbido()? 
Lo que sucede es lo siguiente:

```
zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;
```
Sucede que la función wrapper() recibió la la función zumbido() cómo  parámetro y coloca su salida entre los otros dos prints.

Todo lo que sucede se conoce en programación como metaprogramación (metaprogramming), ya que una parte  del programa trata de modificar otra durante el tiempo de compilación. En tanto, un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

### Mejorando la sintaxis

Definitivamente la forma en que decoramos la función es complejo, pero afortunadamente Python lo tiene en cuenta y podemos utilizar decoradores con el símbolo **@**. Volviendo al mismo ejemplo de funcion_decoradora(), podemos simplificarlo así:

```python
@funcion_decoradora
def zumbido():
    print("Buzzzzzz")
```

## ¿Qué son getters y setters?

En Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos. Un concepto inportante previo a los metodos especificos son las variables privadas, que se definen en Python colocando un guion bajo al inicio de estas (_), normalmente son utilizadqs para añadir lógica de validación al momento de obtener y definir un valor y, para evitar el acceso directo al campo de una clase.

La realidad es que en Python no existen variables netamente privadas, pues aunque se declaren con un guión bajo podemos seguir accediendo a estas. En Programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna clase y tener efectos colaterales que afecten la lógica de nuestra aplicación.

### Clases sin getters y setters

Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas (mi) y lo convierte a kilómetros (km):

```python
class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

         Ahora creemos un objeto que haga referencia a un viaje:

            # Creamos un nuevo objeto
            avion = Millas()

            # Indicamos la distancia
            avion.distancia = 200

            # Obtenemos el atributo distancia
            >>> print(avion.distancia)
            200

            # Obtenemos el método convertir_a_kilometros
            >>> print(avion.convertir_a_kilometros())
            321.8688
```

### Utilizando getters y setters

Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa. Estos son métodos getters y setters:

```python
class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

    # Método getter
    def obtener_distancia(self):
        return self._distancia

    # Método setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        self._distancia = valor
```

El método getter obtendrá el valor de la distancia  y el método setter se encargará de añadir una restricción. También debemos notar cómo distancia fue reemplazado por _distancia, denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizada. Esto no es nada escalable si tenemos cientos o miles de líneas de código.

### Función property()

Esta función está incluida en Python, en particular crea y retorna la propiedad de un objeto. La propiedad  de un objeto posee los métodos getter(), setter() y del().
En tanto la función tiene cuatro atributos: property(fget, fset, fsel, fdoc)

- **fget** : trae el valor de un atributo.
- **fset** : define el valor de un atributo.
- **fdel** : elimina el valor de un atributo.
- **fdoc** : crea un docstring por atributo.

Veamos un ejemplo del mismo caso implementando la función property() :

```python
class Millas:
    def __init__(self):
        self._distancia = 0

    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido

    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

    avion = Millas()
    avion.distancia = 200
    print(avion.distancia)

    Llamada al método getter
    Llamada al método setter
    200
```

Aunque en este ejemplo hay una solo print, tenemos tres líneas como salida pues esta llama a los primeros dos métodos. Por lo que la propiedad distancia es una propiedad de objeto que ayuda a mantener el acceso de forma privada.

### Decorador @property
Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar getters y setters para hacer más fácil  la implementación de la programación orientada a objetos en Python cambiando los métodos o atributos de las clases de forma que no modifiquemos el código.

Pero mejor veamos un ejemplo en acción:

```python
class Millas:
    def __init__(self):
        self._distancia = 0

    @property
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

   
    @obtener_distancia.setter
    def definir_distancia(self, valor)
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor


avion = Millas()
avion.distancia = 200
print(avion.distancia)
```

```
Llamada al método getter
Llamada al método setter
200
```
De esta manera usamos el decorador **@property** para utilizar getters y setters de una forma más prolija e incluimos una nueva funcionalidad a nuestro método definir_distancia(), al mismo tiempo protegemos el acceso a nuestras variables privadas y cumplimos  con el principio de encapsulación.

