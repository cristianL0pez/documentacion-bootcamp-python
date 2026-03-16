# TIPOS DE DATOS EN PYTHON

## 📘 Definición

Los tipos de datos en Python indican qué clase de valor se está almacenando en una variable. Esto es importante porque no es lo mismo trabajar con un texto, un número entero, un número decimal o un valor lógico. Cada tipo de dato tiene un comportamiento distinto dentro del programa.

---

## 🧠 Tipos de datos básicos

### 1. String (`str`)

Se utiliza para representar texto. Va entre comillas simples o dobles.

```python
nombre = "Francisco"
ciudad = "Madrid"
print(nombre)
print(ciudad)
```

### 2. Integer (`int`)

Se utiliza para números enteros, es decir, sin decimales.

```python
edad = 30
cantidad = -5
print(edad)
print(cantidad)
```

### 3. Float (`float`)

Se utiliza para números con decimales.

```python
altura = 1.75
precio = 19.99
print(altura)
print(precio)
```

### 4. Boolean (`bool`)

Se utiliza para representar valores lógicos: `True` o `False`.

```python
es_estudiante = True
tiene_descuento = False
print(es_estudiante)
print(tiene_descuento)
```

---

## 🔍 Cómo saber el tipo de dato

Python permite comprobar el tipo de dato de una variable con la función `type()`.

```python
nombre = "Ana"
edad = 25
altura = 1.68
estudia_python = True

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(estudia_python))
```

---

## ✅ Resumen

Los tipos de datos básicos en Python permiten clasificar la información que se usa en un programa. Los más comunes son `str` para texto, `int` para enteros, `float` para decimales y `bool` para valores lógicos. Comprender estos tipos es fundamental para escribir programas correctamente.
