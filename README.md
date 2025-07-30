decotools es una librería liviana de decoradores para Python que expone utilidades funcionales y expresivas listas para usarse. Todos los decoradores están diseñados para mejorar la ergonomía del código, reducir el boilerplate, y cubrir casos comunes como caching, manejo de errores, evaluación diferida, trazabilidad, composición funcional, entre otros. A continuación se listan todos los decoradores disponibles junto con un ejemplo de uso para cada uno. Importa todo directamente desde el paquete `decotools`, ya que solo los decoradores están expuestos públicamente.

## **@cache**  
Memoiza el resultado de una función basándose en sus argumentos posicionales. Ideal para funciones determinísticas.

```python
from decotools import cache

@cache
def suma(a, b):
    print("Ejecutando...")
    return a + b

suma(2, 3)  # Ejecuta
suma(2, 3)  # Recupera de la caché

```
## **@debug**
Imprime los argumentos y el valor de retorno cada vez que se llama a la función.

````python
from decotools import debug

@debug
def saluda(nombre):
    return f"Hola {nombre}"

saluda("Ana")  # Imprime: saluda(Ana) = Hola Ana
````

## **@deprecate**
Muestra una advertencia con un mensaje cuando se llama a la función.

````python
from decotools import deprecate

@deprecate
def funcion_legacy():
    return 123

funcion_legacy()  # Warning!!
````

## **@lazy**  
Convierte el resultado de una función en una expresión diferida que solo se evalúa cuando se accede a su valor. En lugar de ejecutar la función inmediatamente, `@lazy` devuelve un objeto especial que actúa como un valor simbólico. Este objeto puede participar en operaciones matemáticas (como suma, resta, multiplicación, etc.) sin que se evalúen sus dependencias hasta que se accede explícitamente a `.value`.

Esto es útil para evitar cómputos innecesarios o costosos hasta que realmente se necesitan. Es especialmente valioso en contextos como construcción de expresiones perezosas, evaluaciones condicionales o álgebra simbólica.

```python
from decotools import lazy

@lazy
def obtener_precio():
    print("Consultando API...")
    return 100

@lazy
def descuento():
    return 20

total = obtener_precio() - descuento()
print(total) # Imprime: <SymbolicObject || obtener_precio - descuento>
print(total.value)  # Ahora sí imprime: Consultando API... y luego 80
````

## **@pipeable**
Permite encadenar funciones usando | o >> para composición funcional.
````python
from decotools import pipeable

@pipeable
def duplicar(x):
    return x * 2

@pipeable
def incrementar(x):
    return x + 1

print(3 | duplicar | incrementar)  # Imprime: 7
````

## **@serialize_to('json')**
Serializa el resultado de una función al formato JSON.
````python
from decotools import serialize_to

@serialize_to('json')
def obtener_datos():
    return {'ok': True}

print(obtener_datos())  # {"ok": true}
````
## **@inject_globals**
Inserta variables de entorno automáticamente si no son provistas como argumento.
````python
from decotools import inject_globals
import os

os.environ['API_KEY'] = 'secret'

@inject_globals
def usar_api(API_KEY=None):
    return f"Usando {API_KEY}"

print(usar_api())  # Usa API_KEY de entorno
````

## **@safe**
Atrapa cualquier excepción y retorna None, imprimiendo el error.
````python
from decotools import safe

@safe
def divide(x, y):
    return x / y

print(divide(10, 0))  # None, imprime división por cero
````

## **@partial_safe(exceptions)**
Versión controlada de @safe que solo captura ciertas excepciones.
````python
from decotools import partial_safe

@partial_safe(ZeroDivisionError)
def dividir(x, y):
    return x / y

print(dividir(1, 0))  # None
````
## **@on_exception(callback)**
Ejecuta un callback alternativo si ocurre cualquier excepción.
````python
from decotools import on_exception

@on_exception(lambda: "valor por defecto")
def puede_fallar():
    raise Exception()

print(puede_fallar())  # valor por defecto
````
## **@once**
Garantiza que la función se ejecute una sola vez.
````python
from decotools import once

@once
def init():
    print("Inicializando...")

init()  # Imprime
init()  # No hace nada
````
## **@retry(n, exceptions)**
Reintenta ejecutar una función hasta n veces si lanza alguna excepción.
````python
from decotools import retry

contador = {'intentos': 0}

@retry(3)
def fragil():
    contador['intentos'] += 1
    raise ValueError("Error temporal")

try:
    fragil()
except:
    print(contador['intentos'])  # 3
````
## **@n_times(n)**
Ejecuta la función exactamente n veces.
````python
from decotools import n_times

@n_times(3)
def hola():
    print("Hola")

hola()  # Imprime "Hola" tres veces
````