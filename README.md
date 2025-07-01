# Programación Orientada a Objetos (POO)
Uno de los elementos más importantes de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos. La clave para entender la programación orientada a objetos es pensar en los objetos como agrupaciones de datos y en qué métodos se usarán para operar dichos datos.

Podemos representar a una persona con propiedades como nombre, edad, género, etc. Y los comportamientos de dicha persona como caminar, cantar, comer, etc.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print(f"{self.nombre} está caminando")
```

De la misma manera, podemos representar unos audífonos con propiedades como su marca, tamaño, color, etc., y sus comportamientos como reproducir música, pausar y avanzar a la siguiente canción.

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

Hasta ahora, en las publicaciones y blogs anteriores, hemos utilizado programación orientada a objetos de manera implícita. Hemos utilizado los tipos lista y diccionario, entre muchos otros, así como los métodos asociados a dichos tipos. Los creadores de un lenguaje de programación solo pueden diseñar una fracción muy pequeña de todas las funciones útiles (como ```abs```, ```float```, ```type```, etc.); también pueden escribir una fracción muy pequeña de los tipos útiles (```int```, ```str```, ```dict```, ```list```, etc.). Ya sabemos los mecanismos que nos permiten crear funciones; ahora veremos los mecanismos que nos permiten crear nuevos tipos o clases.

## Historia
La POO tiene sus raíces en varios hitos importantes:

- **1967**: Simula 67, primer lenguaje con características de POO.
- **1972**: Smalltalk, desarrollado en Xerox PARC (Alan Kay).
- **1983**: C++, como extensión de C con POO (Bjarne Stroustrup).
- **1995**: Java populariza la POO en entornos empresariales.

Según un estudio de IEEE de 2020, el 86 % de los lenguajes modernos soportan la POO como paradigma principal, lo que demuestra su relevancia actual.

## Clases en Python
Las estructuras primitivas con las que hemos trabajado hasta ahora nos permiten definir cosas sencillas, como el costo de algo, el nombre de un usuario, las veces que debe correr un bucle, etc. Sin embargo, existen ocasiones en las que necesitamos definir estructuras más complejas, por ejemplo, un hotel. Podríamos utilizar dos listas: una para definir los cuartos y una segunda para definir si el cuarto se encuentra ocupado o no. Este tipo de organización rápidamente se sale de control. ¿Qué tal si quisiéramos añadir más propiedades, como si el cuarto ya fue aseado o no? ¿O si el cuarto tiene cama doble o sencilla? Esto nos lleva a una fuerte falta de organización, y es justamente el punto que justifica la existencia de las clases.

### Ejemplo hotel sin Clases
```python
cuartos_de_hotel = [101, 102, 103]
cuarto_ocupado = [True, False, False]
cuarto_aseado = [False, True, True]
```
Las clases nos permiten crear nuevos tipos que contienen información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases, ```Hotel()``` y ```Habitacion()```, que nos permitan dar seguimiento a propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.


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
Es importante resaltar que las clases solo proveen estructura. Son un molde con el cual podemos construir objetos específicos. La clase señala las propiedades que los hoteles que modelemos tendrán, pero no representa ningún hotel en particular. Para eso necesitamos las instancias.

## Instancias
Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos en nuestro programa: un hotel llamado ```Hotel```. Otra forma de pensarlo es que las clases son como un formulario, y una vez que se llena cada copia del formulario, tenemos las instancias que pertenecen a dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia es distinta de las demás (aunque todas pertenecen a una misma clase).

Para definir una clase, simplemente utilizamos la palabra clave ```class```.

```python  
    class Hotel:
        pass
```
Una vez que tenemos una clase llamada ```Hotel```, podemos generar una instancia llamando al constructor de la clase:
 
```python  
 hotel = Hotel()
```
### Atributos de la instancia:
Todas las clases crean objetos, y todos los objetos tienen atributos. Utilizamos el método especial ```__init__``` para definir el estado inicial de nuestra instancia.
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
Mientras que los atributos de la instancia describen lo que representa el objeto, los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y, normalmente, operan sobre los atributos mencionados.
Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben ```self``` como primer argumento.

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

## Tipos de datos abstractos
En Python, todo elemento es un objeto que pertenece a un tipo específico. Estos objetos permiten tres interacciones fundamentales:
- Creación: Construcción del objeto mediante su inicialización.
- Manipulación: Operaciones que modifican su estado interno.
- Destrucción: Liberación de recursos (automática en Python).

### Ventajas clave
- Descomposición: Dividir sistemas complejos en componentes manejables.
- Abstracción: Enfocarse en características esenciales ignorando detalles técnicos.
- Encapsulación: Proteger datos internos exponiendo solo interfaces controladas.

## Descomposición: Estrategia de Diseño
Técnica para resolver problemas complejos mediante:
- División modular: Crear componentes especializados.
- Jerarquías lógicas: Organizar responsabilidades entre clases.
- Acoplamiento mínimo: Reducir dependencias entre partes.

**Resultado:** Código mantenible y escalable, donde cada clase gestiona una funcionalidad específica.

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
- Enfoque selectivo: Priorizar la información relevante para el contexto.
- Ocultamiento técnico: Ocultar detalles de implementación complejos.
- Interfaces claras: Exponer métodos públicos para una interacción controlada.

### Un ejemplo 
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
## Analizando un poco de lo anterior
- Mientras que la clase es un molde, los objetos creados se conocen como instancias.
- Cuando se crea una instancia, se ejecuta el método ```__init__```.
- Todos los métodos de una clase reciben implícitamente como primer parámetro ```self```.
- Los atributos de clase nos permiten:
    - Representar datos.
    - Definir procedimientos para interactuar con los métodos.
    - Implementar mecanismos para ocultar la representación interna.
- Se accede a los atributos con la notación de punto .
- Puede haber atributos privados. Por convención, comienzan con ```_```.

## FUNCIONES: Bases de los Decoradores
Los decoradores son una forma sencilla de utilizar funciones de orden superior, es decir, funciones que toman otra función como parámetro y/o retornan otra función como resultado.
De esta forma, un decorador añade capacidades a una función sin modificarla.

Un ejemplo de esto son las llantas de un automóvil: si les colocas cadenas para la nieve, aún puede andar, pero extiende su funcionalidad para conducirse en otros terrenos.

## Funciones cómo objetos de primera-clase
Otro concepto importante a tener en cuenta es que en Python las funciones son objetos de primera clase, es decir, pueden ser pasadas y utilizadas como argumentos al igual que cualquier otro objeto (```strings```, ```enteros```, ```flotantes```, ```listas```, etc.).

Un ejemplo donde se definen tres funciones que trabajan de manera conjunta:

```python
def presentarse(nombre):
    return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
    return funcion_entrante("David")
```
Las dos primeras funciones son claras en su resultado: muestran un mensaje con el valor de la variable ```nombre```.
La tercera función puede ser menos predecible, ya que toma una función como entrada. Veamos qué pasa cuando pasamos una función como argumento:

```
consume_funciones(presentarse)
'Me llamo David'

consume_funciones(estudiemos_juntos)
'¡Hey David, aprendamos Python!'
```
Así, la función ```consume_funciones()``` se ejecuta, mientras que las funciones ```presentarse``` y ```estudiemos_juntos``` solo se referencian, sin llamarlas directamente.

## Funciones anidadas
Al igual que los condicionales y bucles, también puedes colocar funciones dentro de otra función. 
Analizá el siguiente código:
```python
def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash y Flask.")
```
                
Si llamamos a la función ```funcion_mayor```, tendremos la siguiente salida:

```SCSS
funcion_mayor()
Esta es una función mayor y su mensaje de salida.
Algunos frameworks de Python son: Django, Dash y Flask.
Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.
```

Debemos considerar que las funciones anidadas dentro de ```funcion_mayor``` no se ejecutan sino hasta que se llama esta primera, lo cual es una muestra del scope o alcance de las funciones. Si intentamos llamar directamente a esas funciones anidadas desde fuera, obtendremos un error.

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

¿Qué pasará si se llama a la función ```zumbido()```?

```SCSS
zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;
```
Sucede que la función wrapper() recibió la función zumbido() como parámetro y colocó su salida entre los otros dos print().

Todo lo que sucede se conoce en programación como metaprogramación (metaprogramming), ya que una parte del programa trata de modificar otra durante el tiempo de compilación. En tanto, un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

### Mejorando la sintaxis

Definitivamente, la forma en que decoramos la función es compleja, pero afortunadamente Python lo tiene en cuenta, y podemos utilizar decoradores con el símbolo ```@```. Volviendo al mismo ejemplo de ```funcion_decoradora()```, podemos simplificarlo así:

```python
@funcion_decoradora
def zumbido():
    print("Buzzzzzz")
```

## ¿Qué son getters y setters?

En Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos. Un concepto inportante previo a los metodos especificos son las variables privadas, que se definen en Python colocando un guion bajo al inicio de estas (_), normalmente son utilizadqs para añadir lógica de validación al momento de obtener y definir un valor y, para evitar el acceso directo al campo de una clase.

La realidad es que en Python no existen variables netamente privadas, pues aunque se declaren con un guión bajo podemos seguir accediendo a estas. En Programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna clase y tener efectos colaterales que afecten la lógica de nuestra aplicación.

### Clases sin getters y setters

Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas ```(mi)``` y lo convierte a kilómetros ```(km)```:

```python
class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)
```

Ahora creemos un objeto que haga referencia a un viaje:

```python
avion = Millas()
avion.distancia = 200
print(avion.distancia)  # 200
print(avion.convertir_a_kilometros())  # 321.8688
```

### Utilizando getters y setters

Incluyamos un par de métodos: uno para obtener la distancia y otro para evitar valores negativos, ya que no tendría sentido que un vehículo recorra una distancia menor a cero. 
Estos son métodos **getter** y **setter**:

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

El método **getter** obtiene el valor de la distancia, y el método **setter** se encarga de añadir una restricción.
También debemos notar cómo ```distancia``` fue reemplazada por ```_distancia```, denotando que es una variable privada.

Si probamos nuestro código, funcionará. Sin embargo, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizada. Esto no es escalable si tenemos cientos o miles de líneas de código.

### Función ```property()```

Esta función está incluida en Python; en particular, crea y retorna la propiedad de un objeto.
La propiedad de un objeto puede contar con los métodos ```getter()```, ```setter()``` y ```del()```.
Esta función acepta cuatro atributos: ```property(fget, fset,fdel,fdoc)```:

- **fget**: trae el valor de un atributo.
- **fset**: define el valor de un atributo.
- **fdel**: elimina el valor de un atributo.
- **fdoc**: crea un docstring para el atributo.

Veamos un ejemplo del mismo caso, ahora implementando la función ```property()```:

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

```
```SCSS
    Llamada al método getter
    Llamada al método setter
    200
```

Aunque en este ejemplo solo hay un ```print```, tenemos tres líneas como salida, pues esta línea llama implícitamente a los dos métodos.
La propiedad ```distancia``` es, entonces, una propiedad de objeto que ayuda a mantener el acceso de forma controlada y privada.

### Decorador ```@property```
Este decorador es uno de los varios que ya incluye Python.
Nos permite utilizar **getters** y **setters** de forma más elegante y sencilla, facilitando la implementación de la programación orientada a objetos en Python sin modificar la estructura del código base.

Veamos un ejemplo en acción:
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

```SCSCC
Llamada al método getter
Llamada al método setter
200
```
De esta manera, usamos el decorador ```@property``` para implementar getters y setters de forma más prolija, agregando lógica adicional (como validaciones) al método ```obtener_distancia```.
Así, protegemos nuestras variables privadas y cumplimos con el principio de encapsulación.

## Encapsulación
- Permite agrupar datos y su comportamiento.
- Controla el acceso a dichos datos.
- Previene modificaciones no autorizadas.

```python
class VotingBooth:

    def __init__(self, id, country):
        self._id = id
        self._country = country
        self._region = None

    @property
    def region(self):
        """Getter para la región (fget)"""
        return self._region

    @region.setter
    def region(self, region):
        """Setter con validación (fset)
        Raises:
            ValueError: Si la región no existe en el país
        """
        if region in self._country:
            self._region = region
        else:
            raise ValueError(f'La región {region} no es válida en {self._country}')

if __name__ == "__main__":
    # Prueba de funcionamiento
    booth = VotingBooth(123, ['Ciudad de México', 'Morelos'])
    print(f"Región inicial: {booth._region}")

    # Asignación válida
    booth.region = 'Ciudad de México'
    print(f"Región asignada: {booth.region}")

    # Intento de asignación inválida
    try:
        booth.region = 'Jalisco'
    except ValueError as e:
        print(f"Error: {e}")
```

## Herencia
- Permite modelar una jerarquía de objetos (clases).
- Permite compartir comportamiento común en la jerarquía.
- A la clase padre se le conoce como superclase y a la clase hija como subclase.
  
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Llama al constructor de Rectangle

if __name__ == "__main__":
    # Demostración con rectángulo
    rectangle = Rectangle(width=3, height=4)
    print(f"Área del rectángulo: {rectangle.area()}")

    # Demostración con cuadrado (usa herencia)
    square = Square(side=5)
    print(f"Área del cuadrado: {square.area()}")
```

## Polimorfismo
- Es la habilidad de tomar varias formas.
- En Python, nos permite cambiar el comportamiento de una superclase para adaptarlo en la subclase.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} está caminando')

class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)  #Llama al constructor de Person

    def move(self):  # Sobreescribe el método de Person
        print(f'{self.name} está moviéndose en bicicleta')

def main():
    # Demostración de polimorfismo
    person = Person('David')
    person.move()  # Output: David esta caminando

    cyclist = Cyclist('Daniel')
    cyclist.move()  #Output: Daniel está en bicicleta

    # Polimorfismo en acción
    for character in [person, cyclist]:
        character.move()  # Mismo método, comportamientos diferentes

if __name__ == "__main__":
    main()
```

## Complejidad Algorítmica (Big O Notation)
- ¿Por qué comparamos la eficiencia de un algoritmo? Porque en la realidad existen billones de datos por analizar. A la hora de procesar grandes volúmenes, la eficiencia es crucial.
- Complejidad temporal vs complejidad espacial: tiempo de procesamiento vs uso de memoria.
- Podemos definirla como t(n), donde n es el tamaño de la entrada.

### CLases de complejidad algoritmica
- O(1): Constante
- O(n): Lineal
- O(Log n): Logaritmica
- O(n log n): Logaritmica Lineal
- O(n**2): Polinomial o cuadratica
- O(2**n): Exponencial


  ### Ejemplo 1: ```O(n)``` – Complejidad lineal
- Dos bucles simples: ```O(n) + O(n) = O(2n)``` → se simplifica a ```O(n)```
- El crecimiento es proporcional al tamaño de la entrada.

```python
def example_linear(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
```

### Ejemplo 2:  ```O(n²)``` – Complejidad cuadrática
- Bucle simple ```O(m)``` + bucle anidado ```O(n²)``` → ```O(m + n²)``` → si m ≈ n, se simplifica a ```O(n²)```
- El término dominante es ```n²```.

```python
def example_quadratic(n, m):
    for i in range(m):
        print(i)
    for i in range(n*n):
        print(i)
```

#### Ejemplo 3: ```O(n²)``` – Complejidad cuadrática
- Bucle anidado: ```O(n) * O(n) = O(n²)```.
- Crecimiento proporcional al cuadrado del tamaño de entrada.

```python
def example_nested_loops(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
```

#### Ejemplo 4: ```O(2ⁿ)``` – Complejidad exponencial
- Función recursiva con llamadas múltiples (ejemplo: Fibonacci).
- El crecimiento es exponencial, formando un árbol de recursión binario.

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Algoritmos de Búsqueda y Ordenación
El objetivo es aplicar los conceptos de complejidad algorítmica y entender que existen diferentes algoritmos para resolver problemas, dependiendo del contexto, la cantidad de datos y la eficiencia requerida.

### Búsqueda Lineal
- Busca el elemento de forma secuencial, comparando uno por uno.
- Es útil para listas pequeñas o no ordenadas, pero su eficiencia disminuye con listas grandes.
- Complejidad: ```O(n)``` en el peor caso.

```python
import random
def linear_search(list, target):
    found = False
    for element in list:
        if element == target:
            found = True
            break  # Optimización que no cambia la complejidad O(n)
    return found

if __name__ == "__main__":
    list_size = int(input('¿De qué tamaño será la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(list)
    is_found = linear_search(list, target)
    print(f'El elemento {target} {"está" if is_found else "no está"} en la lista')
```

### Búsqueda Binaria (solo para listas ordenadas)
- Aplica la estrategia de divide y vencerás.
- En cada iteración, reduce el problema a la mitad, comparando con el valor medio.
- Mucho más eficiente que la búsqueda lineal, pero requiere que la lista esté ordenada.
- Complejidad: ```O(log n)```

```python
import random

def binary_search(sorted_list, start, end, target):
    print(f'Searching {target} between {sorted_list[start]} and {sorted_list[end-1]}')
    if start > end:
        return False
    mid = (start + end) // 2
    if sorted_list[mid] == target:
        return True
    elif sorted_list[mid] < target:
        return binary_search(sorted_list, mid+1, end, target)
    else:
        return binary_search(sorted_list, start, mid-1, target)

if __name__ == "__main__":
    list_size = int(input('What size should the list be? '))
    target = int(input('What number to find? '))
    sorted_list = sorted([random.randint(0,100) for _ in range(list_size)])
    print(sorted_list)
    found = binary_search(sorted_list, 0, len(sorted_list), target)
    print(f'Element {target} {"is" if found else "is not"} in the list')
```

### Ordenamiento de Burbuja
- Recorre repetidamente la lista y compara elementos adyacentes, intercambiándolos si están en el orden incorrecto.
- Este proceso se repite hasta que no se requieren más intercambios, indicando que la lista está ordenada.
- Es simple de entender pero poco eficiente en listas grandes.
- Complejidad: ```O(n²)``` en el peor caso.

```python
import random

def bubble_sort(list):
    length = len(list)
    for i in range(length):  # O(n) pasadas
        for j in range(0, length - i - 1):  # O(n) comparaciones
            if list[j] > list[j+1]:
                # Intercambio de elementos
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(f"Lista original: {list}")

    sorted_list = bubble_sort(list.copy())  # Usamos copy() para no modificar la original
    print(f"Lista ordenada: {sorted_list}")
```

### Ordenamiento por inserción
El ordenamiento por inserción es uno de los algoritmos más sencillos y conocidos en informática. Es ideal para aprender los fundamentos de algoritmos de ordenamiento debido a su lógica intuitiva y su implementación directa. Sin embargo, no es eficiente para listas grandes, ya que su rendimiento disminuye a medida que crece la cantidad de datos.

Una de las características del ordenamiento por inserción es que ordena "en el lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento ya que simplemente modifican los valores en memoria.

**Cómo funciona?**
El algoritmo divide la lista en dos partes:
- Una sublista ordenada (al principio solo contiene un elemento).
- Una sublista desordenada (el resto de la lista).

El proceso consiste en tomar uno a uno los elementos de la sublista desordenada e insertarlos en la posición correcta dentro de la sublista ordenada.


**Paso a paso**:
1. Consideramos el primer elemento como la sublista ordenada.
2. Tomamos el siguiente elemento (al que llamaremos ```valor_actual```).
4. Lo comparamos con los elementos anteriores.
5. Si ```valor_actual``` es menor, movemos los elementos mayores una posición a la derecha.
6. Insertamos ```valor_actual``` en la posición correcta.
7. Repetimos hasta que toda la lista esté ordenada.

**Ejemplo**
Dada la lista:
```csharp
[7, 3, 2, 9, 8]
```
Iteración 1:
- Sublista ordenada:```[7]```
- Sublista desordenada: ```[3, 2, 9, 8]```
- valor_actual = 3, como 3 < 7, movemos el 7 a la derecha e insertamos 3:

```csharp
[3, 7, 2, 9, 8]
```
Iteración 2:
- valor_actual = 2, lo comparamos con 7 y 3, ambos son mayores, los movemos y colocamos 2 en la primera posición:

```csharp
[2, 3, 7, 9, 8]
```
Iteración 3:
- valor_actual = 9, ya está en la posición correcta (mayor que todos los anteriores):

```csharp
[2, 3, 7, 9, 8]
```
Iteración 4:
- valor_actual = 8, es menor que 9, así que lo movemos y colocamos 8 en su lugar:

```csharp
[2, 3, 7, 8, 9]
```

**Implementación en Python**

```python
import random

def insertion_sort(list):
    for index in range(1, len(list)):  # Comenzamos desde 1 (corrección)
        current_value = list[index]
        current_position = index
        print(f"Valor actual: {current_value}, Posición: {current_position}")

        # Mover elementos mayores hacia la derecha
        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1
            list[current_position] = current_value
            print(f"Paso intermedio: {list}")

    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print(f"Lista original: {list}")

    sorted_list = insertion_sort(list.copy())  # Usamos copy() para no modificar la original
    print(f"Lista ordenada: {sorted_list}")
```
### Ordenamiento por Mezcla (Merge Sort)
El ordenamiento por mezcla es un algoritmo clásico basado en la estrategia de "divide y vencerás". A diferencia del ordenamiento por inserción, este enfoque no ordena en su lugar, sino que divide la lista en partes más pequeñas, las ordena individualmente y luego las fusiona de forma ordenada.

**¿Cómo funciona?**

- Dividir: La lista original se divide recursivamente en dos mitades hasta obtener sublistas de 1 o 0 elementos (las cuales, por definición, ya están ordenadas).

- Conquistar (Ordenar y combinar): Luego, esas sublistas se van fusionando dos a dos, comparando elementos y construyendo nuevas listas ordenadas hasta reconstruir la lista original completamente ordenada.

Este algoritmo tiene una complejidad temporal de O(n log n) en todos los casos, lo que lo hace muy eficiente para listas grandes.

```python
import random

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left, '*' * 8, right)

        # Llamadas recursivas para dividir cada mitad
        merge_sort(left)
        merge_sort(right)

        # Variables para recorrer las sublistas y fusionar
        i = j = k = 0

        # Comparar y fusionar elementos ordenadamente
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        # Agregar los elementos restantes de left (si hay)
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        # Agregar los elementos restantes de right (si hay)
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        # Visualización del proceso
        print(f'Left {left}     Right {right}')
        print(f'Mezclado: {list}')
        print('*' * 40)

    return list

if __name__ == "__main__":
    list_size = int(input('Ingrese el tamaño de la lista: '))
    list = [random.randint(0, 100) for _ in range(list_size)]
    print("\nLista original:", list)
    print('-' * 30)

    sorted_list = merge_sort(list.copy())
    print("\nLista ordenada:", sorted_list)
```
