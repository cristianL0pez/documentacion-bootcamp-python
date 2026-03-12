# CONTROL DE FLUJO: LOOPS

> Autor: Alex Martinez (gambito700)
> Fecha: 11 de marzo de 2026
> Issue relacionada: #10

---

## 📘 Definición

Los loops son estructuras de control que permiten repetir un bloque de codigo multiples veces.
En Python existen 2 tipos de loops y 4 modificadores:

loops:
- `for`   → itera sobre una secuencia de elementos uno por uno
- `while` → repite un bloque mientras la condicion sea verdadera

modificadores:
- `break`    → sale del loop inmediatamente
- `continue` → salta la iteracion actual y continua con la siguiente
- `pass`     → no hace nada, es un placeholder
- `else`     → se ejecuta cuando el loop termina sin break

---

## 🧠 ¿Para qué sirve?

Sirven para automatizar tareas repetitivas. Son fundamentales porque permiten:

1. Recorrer listas: iterar sobre cada elemento de una coleccion de datos.
2. Repetir procesos: ejecutar una operacion hasta que se cumpla una condicion.
3. Reducir codigo: evitar escribir el mismo bloque multiples veces.
4. Controlar flujo: decidir cuando pausar, saltar o detener una iteracion.

---

## 🧩 Sintaxis

### FOR - 4 formas comunes
- Numerica          `for n in range(x)`
- Lista             `for tree in carpetas`
- Con indice        `for i, tree in enumerate(carpetas)`
- Multiples listas  `for a, b in zip(lista1, lista2)`

**FOR con RANGO numerico**
- `for`        inicia el loop
- `n`          es la variable que recibe cada valor de la secuencia
- `in`         indica dentro de que va a iterar
- `range(4)`   genera la secuencia 0, 1, 2, 3
- se comienza desde 0 por lo que range(4) imprimira del 0 al 3
- `print(n)`   imprime el valor actual de n en cada iteracion
```
for n in range(4):
    print(n)
```

Flujo completo:
```
vuelta 1 → n = 0 → imprime 0
vuelta 2 → n = 1 → imprime 1
vuelta 3 → n = 2 → imprime 2
vuelta 4 → n = 3 → imprime 3
no hay mas elementos → se detiene
```

---

**FOR con LISTA**
- `for tree in carpetas`   recorre cada elemento de la lista
- `tree`                   variable receptora, puede llamarse de cualquier forma
- `carpetas`               lista de elementos a recorrer
- `print(tree)`            imprime el valor actual de tree en cada iteracion
```
carpetas = ["C:\\", "control-de-flujo", "estructuras-de-datos", "funciones", "Fundamentos", "modulos", "poo"]

for tree in carpetas:
    print(tree)
```

Flujo completo:
```
vuelta 1 → tree = "C:\\"                  → imprime "C:\\"
vuelta 2 → tree = "control-de-flujo"      → imprime "control-de-flujo"
vuelta 3 → tree = "estructuras-de-datos"  → imprime "estructuras-de-datos"
no hay mas elementos → se detiene
```

---

**FOR con INDICE**
- `for i, tree in enumerate(carpetas)`   recorre la lista enumerando cada elemento con indice
- `i`                                    es el indice o posicion del elemento
- `tree`                                 es el valor del elemento
- `enumerate`                            genera pares (indice, valor) automaticamente
```
for i, tree in enumerate(carpetas):
    print(i, tree)
```

Flujo completo:
```
vuelta 1 → i = 0, tree = "C:\\"                  → imprime "0 C:\\"
vuelta 2 → i = 1, tree = "control-de-flujo"      → imprime "1 control-de-flujo"
vuelta 3 → i = 2, tree = "estructuras-de-datos"  → imprime "2 estructuras-de-datos"
no hay mas elementos → se detiene
```

---

**FOR con ZIP / MULTIPLES LISTAS**
- `for numero, tree, letra in zip(numeros, carpetas, letras)`   recorre multiples listas a la vez
- `numero`   recibe cada elemento de la lista numeros
- `tree`     recibe cada elemento de la lista carpetas
- `letra`    recibe cada elemento de la lista letras
- `zip`      une las listas en pares, se detiene cuando la lista mas corta se acaba
```
numeros = [1, 2, 3, 4, 5, 6, 7]
letras  = ["a", "b", "c", "d", "e", "f", "g", "h"]

for numero, tree, letra in zip(numeros, carpetas, letras):
    print(letra, numero, tree)
```

Flujo completo:
```
vuelta 1 → numero = 1, tree = "C:\\",                 letra = "a" → imprime "a 1 C:\\"
vuelta 2 → numero = 2, tree = "control-de-flujo",     letra = "b" → imprime "b 2 control-de-flujo"
vuelta 3 → numero = 3, tree = "estructuras-de-datos", letra = "c" → imprime "c 3 estructuras-de-datos"
no hay mas elementos → se detiene
```

---

### WHILE - 3 formas comunes
- Numerica    `while contador < 5`
- Con lista   `while x < len(carpetas)`
- Infinito    `while True`

**WHILE con CONTADOR**
- `contador = 0`        variable que almacena el valor inicial
- `while contador < 5`  condicion que evalua si contador es menor que 5
- `print(contador)`     imprime el valor actual de contador en cada iteracion
- `contador += 1`       incrementa contador en 1, sin esto seria un loop infinito
```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Flujo completo:
```
0 < 5 → True  → imprime 0 → contador = 1
1 < 5 → True  → imprime 1 → contador = 2
2 < 5 → True  → imprime 2 → contador = 3
3 < 5 → True  → imprime 3 → contador = 4
4 < 5 → True  → imprime 4 → contador = 5
5 < 5 → False → se detiene
```

---

**WHILE con LISTA**
- `x = 0`                    indice inicial para acceder a los elementos
- `while x < len(carpetas)`  recorre la lista mientras queden elementos
- `len(carpetas)`            devuelve el total de elementos de la lista, en este caso 7
- `carpetas[x]`              accede al elemento en la posicion x
- `x += 1`                   incrementa x en 1, sin esto seria un loop infinito
```
x = 0
while x < len(carpetas):
    print(carpetas[x])
    x += 1
```

Flujo completo:
```
x = 0 → 0 < 7 → True  → imprime "C:\\"                 → x = 1
x = 1 → 1 < 7 → True  → imprime "control-de-flujo"     → x = 2
x = 2 → 2 < 7 → True  → imprime "estructuras-de-datos" → x = 3
x = 7 → 7 < 7 → False → se detiene
```

---

**WHILE con TRUE y BREAK**
- `while True`             repite para siempre hasta que un break lo detenga
- `respuesta`              variable que guarda lo que el usuario escribe
- `input()`                detiene el programa y espera que el usuario escriba algo
- `if respuesta == 'si'`   evalua si el usuario escribio exactamente "si"
- `break`                  si la condicion se cumple, sale del loop inmediatamente
```
while True:
    respuesta = input("Que el bucle termine? : ")
    if respuesta == "si":
        break
    print("bucle continua...")
```

Flujo completo:
```
vuelta 1 → usuario escribe "no"  → imprime "bucle continua..." → repite
vuelta 2 → usuario escribe "no"  → imprime "bucle continua..." → repite
vuelta 3 → usuario escribe "si"  → break → se detiene
```

---

### MODIFICADORES

**BREAK** - interrumpe el loop inmediatamente al cumplirse la condicion
```
for n in range(10):
    if n == 5:
        break
    print(n)
```
```
n = 0 → 0 != 5 → imprime 0
n = 4 → 4 != 5 → imprime 4
n = 5 → 5 == 5 → break → se detiene
```

---

**CONTINUE** - salta la iteracion actual y pasa a la siguiente
```
for n in range(10):
    if n == 5:
        continue
    print(n)
```
```
n = 4 → 4 != 5 → imprime 4
n = 5 → 5 == 5 → continue → salta al siguiente
n = 6 → 6 != 5 → imprime 6
```

---

**PASS** - no hace nada, es un marcador de posicion
```
for n in range(5):
    if n == 3:
        pass
    print(n)
```
```
n = 2 → imprime 2
n = 3 → pass → no hace nada → imprime 3 igual
n = 4 → imprime 4
```

---

**ELSE** - se ejecuta cuando el loop termina sin un break
```
for n in range(5):
    print(n)
else:
    print("el loop termino normalmente")

for n in range(5):
    if n == 3:
        break
else:
    print("esto NO se imprime porque hubo un break")
```
```
sin break → loop termina normalmente → else se ejecuta
con break → loop se interrumpe       → else NO se ejecuta
```


# FIN #