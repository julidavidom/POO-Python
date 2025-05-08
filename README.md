# Programación Orientada a Objetos (POO)

## Introducción a la POO

La **Programación Orientada a Objetos** (POO) es un paradigma de programación que utiliza **clases** para organizar programas en módulos y abstracciones de datos. Según Grady Booch en su libro *Object-Oriented Analysis and Design with Applications*, "La POO es un método de implementación en el que los programas están organizados como colecciones cooperativas de objetos, cada uno de los cuales representa una instancia de alguna clase".

### Conceptos Fundamentales
- **Objetos**: Agrupaciones de datos (atributos) y métodos que operan sobre esos datos
- **Clases**: Plantillas para crear objetos, definiendo estructura y comportamiento

**Ejemplos del mundo real**:
```python
# Ejemplo de clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def caminar(self):
        print(f"{self.nombre} está caminando")

# Ejemplo de clase Audífonos
class Audifonos:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def reproducir(self):
        print("Reproduciendo música...")
```
## Historia y Evolución (Contexto Académico)
La POO tiene sus raíces en varios hitos importantes:

- **1967:** Simula 67, primer lenguaje con características de POO.
- **1972:** Smalltalk desarrollado en Xerox PARC (Alan Kay).
- **1983:** C++ como extensión de C con POO (Bjarne Stroustrup).
- **1995:** Java populariza la POO en entornos empresariales. 

Según un estudio de IEEE de 2020, el 86% de los lenguajes modernos soportan POO como paradigma principal, demostrando su relevancia actual.

## Clases en Python: De lo Primitivo a lo Complejo
Limitaciones de estructuras simples
```python
# Enfoque problemático sin POO
cuartos_de_hotel = [101, 102, 103]
cuarto_ocupado = [True, False, False]
cuarto_aseado = [False, True, True]
```
Este enfoque viola el principio DRY (Don't Repeat Yourself) y dificulta el mantenimiento.

**Solución con Clases**
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

## Instancias y Atributos: La Esencia de la POO
Diferencias Clave
```markdown
| Clase                 | Instancia               |
|:----------------------|:------------------------|
| Plantilla/Blueprint   | Objeto concreto         |
| Define estructura     | Contiene datos reales   |
| Se define una vez     | Se crean múltiples veces|
```

```python
# Creación de instancias
mi_hotel = Hotel("Platzi Suites")
tu_hotel = Hotel("Hilton")

print(type(mi_hotel))  # <class '__main__.Hotel'>
print(mi_hotel.nombre) # Platzi Suites
```
## Atributos y Métodos: Comportamiento del Objeto
Método**__init__**

```python
class Hotel:
    def __init__(self, capacidad, estacionamientos):
        self.capacidad_maxima = capacidad
        self.estacionamientos = estacionamientos
        self.huespedes = 0  # Atributo de estado
```

## Métodos de Instancia: Comportamientos Clave
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

# Uso
hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
print(f"Ocupación: {hotel.ocupacion_actual()}")  # 3
```

## Tipos de Datos Abstractos (Definidos por el Usuario)
En Python, todo elemento es un objeto que pertenece a un tipo específico. Estos objetos permiten tres interacciones fundamentales:

- Creación: Construcción del objeto mediante su inicialización
- Manipulación: Operaciones que modifican su estado interno
- Destrucción: Liberación de recursos (automática en Python)

**Ventajas clave**
- Descomposición: Dividir sistemas complejos en componentes manejables
- Abstracción: Enfocarse en características esenciales ignorando detalles técnicos
- Encapsulación: Proteger datos internos exponiendo solo interfaces controladas

## Instancias: Objetos en Acción
Relación Clase-Instancia
Clase: Molde abstracto que define estructura y comportamiento
Instancia: Objeto concreto creado desde la clase, con estado único

### Características técnicas
- El método __init__ inicializa el estado al crear la instancia
- **self** referencia a la instancia actual (contexto de ejecución)

### Atributos:
Públicos: Accesibles directamente (instancia.atributo)
Privados por convención: Nombres con _ inicial.


## Descomposición: Estrategia de Diseño
Técnica para resolver problemas complejos mediante:

1. División modular: Crear componentes especializados
2. Jerarquías lógicas: Organizar responsabilidades entre clases
3. Acoplamiento mínimo: Reducir dependencias entre partes

**Resultado:** Código mantenible y escalable donde cada clase gestiona una funcionalidad específica

## Abstracción: Simplificación Efectiva
Principio que permite:

- Enfoque selectivo: Priorizar información relevante para el contexto.
- Ocultamiento técnico: Esconder detalles de implementación complejos.
- Interfaces claras: Exponer métodos públicos para interacción controlada.
