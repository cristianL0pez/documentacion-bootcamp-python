# FUNCIONES: LAMBDA

> Autor: Alex Martinez (gambito700)
> Fecha: 24 de marzo de 2026
> Issue relacionada: #25

---

##  Definición

Una función lambda es una función anónima de una sola línea.
Se usa cuando necesitas una función simple sin necesidad de definirla con ` def `.

funciones normales vs lambda:
- `def`    → función con nombre, cuerpo y return explícito
- `lambda` → función sin nombre, en una sola línea, return implícito

sintaxis básica:
```
lambda parametros : expresion
```

equivalencia:
```
def doble(x):         →   lambda x: x * 2
    return x * 2
```

---

##  ¿Para qué sirven?

Sirven para escribir funciones cortas sin tener que usar `def`. Son fundamentales porque permiten:

1. Simplicidad: reemplazar funciones de una línea con menos código.
2. Funciones en el momento: crear lógica puntual sin nombres ni bloques.
3. Trabajar con otras funciones: usarlas como argumento en `map`, `filter` y `sorted`.
4. Legibilidad: cuando la lógica es simple, una lambda lo expresa más directo.

---

##  Sintaxis

### LAMBDA - 4 formas comunes
- Básica             `lambda x: x * 2`
- Múltiples params   `lambda x, y: x + y`
- Con condicional    `lambda x: "mayor" if x >= 18 else "menor"`
- Con map/filter     `map(lambda x: x * 2, lista)`

**LAMBDA BÁSICA**
- `lambda`   palabra clave que inicia la función anónima
- `x`        parámetro que recibe la función
- `:`        separa los parámetros de la expresión
- `x * 2`    expresión que se evalúa y retorna automáticamente
- `doble`    variable que guarda la lambda para poder llamarla
```
doble = lambda x: x * 2

print(doble(5))
```

Flujo completo:
```
doble(5) → x = 5 → 5 * 2 → retorna 10 → imprime 10
```

---

**LAMBDA con MÚLTIPLES PARÁMETROS**
- `lambda x, y`   recibe dos parámetros separados por coma
- `x + y`         opera con ambos parámetros
```
sumar = lambda x, y: x + y

print(sumar(3, 4))
```

Flujo completo:
```
sumar(3, 4) → x = 3, y = 4 → 3 + 4 → retorna 7 → imprime 7
```

---

**LAMBDA con CONDICIONAL**
- `valor_si_true if condicion else valor_si_false`
- es el operador ternario de Python dentro de una lambda
```
mayor_de_edad = lambda edad: "mayor" if edad >= 18 else "menor"

print(mayor_de_edad(20))
print(mayor_de_edad(15))
```

Flujo completo:
```
mayor_de_edad(20) → edad = 20 → 20 >= 18 → True  → retorna "mayor" → imprime "mayor"
mayor_de_edad(15) → edad = 15 → 15 >= 18 → False → retorna "menor" → imprime "menor"
```

---

### LAMBDA con MAP, FILTER y SORTED

**LAMBDA con MAP** - aplica una función a cada elemento de una lista
- `map(funcion, lista)`   aplica la función a cada elemento
- `list()`                convierte el resultado en lista
- sin `list()` map devuelve un objeto map, no una lista directa
```
numeros = [1, 2, 3, 4, 5]

dobles = list(map(lambda x: x * 2, numeros))

print(dobles)
```

Flujo completo:
```
vuelta 1 → x = 1 → 1 * 2 = 2
vuelta 2 → x = 2 → 2 * 2 = 4
vuelta 3 → x = 3 → 3 * 2 = 6
vuelta 4 → x = 4 → 4 * 2 = 8
vuelta 5 → x = 5 → 5 * 2 = 10
resultado → [2, 4, 6, 8, 10]
```

---

**LAMBDA con FILTER** - filtra elementos que cumplan una condición
- `filter(funcion, lista)`   mantiene solo los elementos donde la función retorna True
- `list()`                   convierte el resultado en lista
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
```

Flujo completo:
```
x = 1  → 1 % 2 = 1 → 1 != 0 → False → descarta
x = 2  → 2 % 2 = 0 → 0 == 0 → True  → mantiene
x = 3  → 3 % 2 = 1 → 1 != 0 → False → descarta
x = 4  → 4 % 2 = 0 → 0 == 0 → True  → mantiene
...
resultado → [2, 4, 6, 8, 10]
```

---

**LAMBDA con SORTED** - ordena una lista usando una clave personalizada
- `sorted(lista, key=funcion)`   ordena según el valor que retorna la función
- `key=lambda`                   define el criterio de ordenamiento
```
nombres = ["carlos", "ana", "beatriz", "david", "el"]

por_largo = sorted(nombres, key=lambda nombre: len(nombre))

print(por_largo)
```

Flujo completo:
```
"carlos"  → len = 6
"ana"     → len = 3
"beatriz" → len = 7
"david"   → len = 5
"el"      → len = 2
ordenados por largo → ["el", "ana", "david", "carlos", "beatriz"]
```

---

**LAMBDA con SORTED y DICCIONARIOS** - muy usado en proyectos reales
- `key=lambda x: x["clave"]`   extrae el valor por el que se ordena
```
alumnos = [
    {"nombre": "carlos", "nota": 55},
    {"nombre": "ana",    "nota": 90},
    {"nombre": "luis",   "nota": 72},
    {"nombre": "maria",  "nota": 88}
]

por_nota = sorted(alumnos, key=lambda alumno: alumno["nota"])

for a in por_nota:
    print(a["nombre"], a["nota"])
```

Flujo completo:
```
carlos → nota 55
luis   → nota 72
maria  → nota 88
ana    → nota 90
resultado ordenado de menor a mayor nota
```

para ordenar de mayor a menor agregar `reverse=True`:
```
sorted(alumnos, key=lambda alumno: alumno["nota"], reverse=True)
```

---

### EJERCICIOS

**EJERCICIO 1** - lambda con map y filter combinados
dada una lista de números, obtener el doble de solo los números impares
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares       = list(filter(lambda x: x % 2 != 0, numeros))
doble_impares = list(map(lambda x: x * 2, impares))

print(doble_impares)
```

Flujo completo filter:
```
x = 1 → 1 % 2 = 1 → True  → mantiene
x = 2 → 2 % 2 = 0 → False → descarta
x = 3 → 3 % 2 = 1 → True  → mantiene
...
impares = [1, 3, 5, 7, 9]
```

Flujo completo map:
```
x = 1 → 1 * 2 = 2
x = 3 → 3 * 2 = 6
x = 5 → 5 * 2 = 10
x = 7 → 7 * 2 = 14
x = 9 → 9 * 2 = 18
resultado → [2, 6, 10, 14, 18]
```

---

**EJERCICIO 2** - ordenar películas por año usando lambda
dada una lista de películas, ordenarlas de más antigua a más reciente
```
peliculas = [
    {"nombre": "matrix",       "anio": 1999},
    {"nombre": "interstellar", "anio": 2014},
    {"nombre": "alien",        "anio": 1979},
    {"nombre": "dune",         "anio": 2021}
]

por_anio = sorted(peliculas, key=lambda p: p["anio"])

for p in por_anio:
    print(p["anio"], "-", p["nombre"])
```

Flujo completo:
```
alien        → anio 1979
matrix       → anio 1999
interstellar → anio 2014
dune         → anio 2021
```

---

### COMPARACIÓN FINAL - def vs lambda

```
# con def:
def elevar_al_cuadrado(x):
    return x ** 2

# con lambda:
elevar_al_cuadrado = lambda x: x ** 2
```
```
ambas hacen lo mismo
usa def    → cuando la lógica es compleja o necesitas reutilizarla mucho
usa lambda → cuando es simple y puntual, especialmente dentro de map, filter o sorted
```

---

### ERROR COMÚN - múltiples líneas en una lambda

lambda solo acepta UNA expresión, no bloques de código
```
# incorrecto:
operar = lambda x:
    resultado = x * 2    → SyntaxError
    return resultado
```
```
# por qué falla:
# lambda no tiene cuerpo con indentación
# si necesitas más de una línea usa def

# correcto:
def operar(x):
    resultado = x * 2
    return resultado
```

Flujo del error:
```
lambda         → espera una expresión en la misma línea
salto de línea → python no lo puede interpretar → SyntaxError
```


# FIN # 
## borrar esto ##

### y esto ###