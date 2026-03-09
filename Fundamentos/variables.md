# FUNDAMENTOS DE VARIABLES EN PYTHON

## 📘 Definición
Una variable es un nombre que funciona como una etiqueta para referirse a un valor guardado en la memoria de la computadora. Si se representaran, serían como "cajas" donde se guarda información para usarla más tarde en un programa.

## 🧠 Sintaxis

Para entender las variables, debemos conocer qué tipos de "objetos" podemos guardar en ellas:
1- Strings (str): Cadenas de texto. Siempre van entre comillas dobles "" o simples ''.
2- Integers (int): Números enteros, positivos o negativos, sin decimales.
3- Floats (float): Números reales que contienen un punto decimal.
4- Booleans (bool): Valores lógicos que solo pueden ser True (Verdadero) o False (Falso).

Para crear una variable, se utiliza el operador de asignación =. A la izquierda va el nombre elegido y a la derecha el valor que se quiere guardar.

Para ver qué hay dentro de tus variables mientras programas, usamos la función print():

```python
# ejemplos simples

# Declaración de variables con distintos tipos de datos
nombre = "Pepito"          # Un String (texto) entre comillas
puntuacion = 10            # Un Integer (número entero)
estatura = 1.75            # Un Float (número decimal)
es_estudiante = True       # Un Boolean (valor lógico)

# Podemos usar las variables llamando a su nombre
print(nombre)              # Salida: Pepito
print(puntuacion + 5)      # Salida: 15

