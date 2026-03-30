# ESTRUCTURAS DE DATOS: DICCIONARIOS  

> Autor: Alex Martinez (gambito700)  
> Fecha: 16 de marzo de 2026  
> Issue relacionada: #17  

---

## Definición

Un diccionario es una estructura de datos que guarda datos en formato **clave : valor**.

En Python existen **5 operaciones principales** y **3 formas de recorrerlos**:

### Operaciones
- **crear**    → define el diccionario con sus pares clave : valor  
- **acceder**  → obtiene un valor usando su clave con `["clave"]`  
- **modificar**→ cambia el valor de una clave existente  
- **agregar**  → agrega un nuevo par clave : valor  
- **eliminar** → borra un par clave : valor con `del` o `.pop()`  

### Recorrido con for
- **keys**   → itera solo las claves  
- **values** → itera solo los valores  
- **items**  → itera claves y valores juntos  

---

## ¿Para qué sirve?

Sirven para organizar datos relacionados bajo un mismo nombre.

Permiten:
1. Agrupar información  
2. Acceso directo  
3. Modificar datos  
4. Recorrer información  

---

## Sintaxis

### Crear diccionario

```python
persona = {
    "nombre"   : "carlos",
    "edad"     : 28,
    "direccion": "calle falsa 123",
    "ciudad"   : "valparaiso"
}
```

---

### Acceder a un valor

```python
print(persona["ciudad"])
```

**Resultado:**
```
valparaiso
```

---

### Modificar un valor

```python
persona["edad"]   = 35
persona["nombre"] = "carla"
```

---

### Agregar un dato

```python
persona["pais"]   = "chile"
persona["altura"] = 190
```

---

### Eliminar datos

#### Con `del`
```python
del persona["altura"]
```

#### Con `.pop()`
```python
valor_eliminado = persona.pop("pais")
```

---

## Recorrer diccionario

### Keys

```python
for k in persona:
    print(k)
```

---

### Values

```python
for v in persona.values():
    print(v)
```

---

### Items

```python
for k, v in persona.items():
    print(k, v)
```

---

## Ejercicio 1

```python
gambito = {
    "nombre": "alex",
    "edad"  : 34,
    "ciudad": "mallolafken"
}

for k in gambito:
    print(k)

for v in gambito.values():
    print(v)

for k, v in gambito.items():
    print(k, v)
```

---

## Ejercicio 2

```python
alumnos = [
    {"nombre": "ana",    "edad": 19},
    {"nombre": "carlos", "edad": 23},
    {"nombre": "luis",   "edad": 17},
    {"nombre": "maria",  "edad": 21}
]

for alumno in alumnos:
    if alumno["edad"] > 20:
        print(alumno["nombre"], alumno["edad"])
```

---

## Proyecto práctico: lista de películas

```python
peliculas = []

while True:
    print("menu")
    print("1. agregar pelicula")
    print("2. borrar pelicula")
    print("3. ver lista")
    print("4. buscar pelicula")
    print("5. salir")

    opcion = input("ingrese la opcion: ")

    if opcion == "1":
        nombre = input("nombre de la pelicula: ")
        genero = input("genero de la pelicula: ")
        anio   = input("anio de la pelicula: ")

        pelicula = {
            "nombre": nombre,
            "anio"  : anio,
            "genero": genero
        }

        peliculas.append(pelicula)
        print("pelicula guardada!")

    elif opcion == "2":
        peli_borrar = input("nombre de la peli a borrar: ")

        for peli in peliculas:
            if peli["nombre"] == peli_borrar:
                peliculas.remove(peli)
                print("peli borrada!")
                break

    elif opcion == "3":
        for peli in peliculas:
            print(peli["nombre"], "-", peli["anio"], "-", peli["genero"])

    elif opcion == "4":
        peli_buscar = input("nombre de la peli a buscar: ")
        encontrada = False

        for peli in peliculas:
            if peli["nombre"] == peli_buscar:
                print("nombre :", peli["nombre"])
                print("anio   :", peli["anio"])
                print("genero :", peli["genero"])
                encontrada = True
                break

        if not encontrada:
            print("pelicula no encontrada")

    elif opcion == "5":
        print("programa terminado!")
        break

    else:
        print("opcion no valida, intenta de nuevo")
```

---

## Error común

### Incorrecto

```python
for peli in peliculas:
    print(peliculas["nombre"])
```

### Correcto

```python
for peli in peliculas:
    print(peli["nombre"])
```

---

## Fin