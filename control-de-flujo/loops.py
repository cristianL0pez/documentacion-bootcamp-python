# importaciones siempre arriba
# import os

#-----------------------------------------------------------------------------------------------#
#----------------------------------------------FOR----------------------------------------------#
#-----------------------------------------------------------------------------------------------#

#"for" itera sobre una secuencia de elementos uno por uno
# en cada vuelta toma un elemento, lo guarda en la variable y ejecuta

# for n in range(4)
# "for"     inicia el loop
# "n"           es la variable que recibe cada valor de la secuencia
# "in"          indica dentro de que va a iterar
# "range(4)"    genera la secuencia 0, 1, 2, 3
# se comienza desde 0 por lo que le pido 4 imprimira del 0 al 3
# print(n)      imprime el valor actual de n en cada iteración

for n in range(4):
    print(n)
    
# Flujo completo
# vuelta 1 → n = 0 → imprime 0
# vuelta 2 → n = 1 → imprime 1
# vuelta 3 → n = 2 → imprime 2
# vuelta 4 → n = 3 → imprime 3
# no hay mas elementos → se detiene

# otras formas de print()
# print(n, end=" ")   separa con espacio
# print(n, end="-")   separa con guión
# print(n, end="x")   en realidad podria ir cualquier cosa
# print(n, end="")    todo junto
# print(n, end="\n")  comportamiento por defecto

# creo la variable "carpetas" con una lista de nombres de carpetas del repositorio
carpetas = ["C:\\", "control-de-flujo", "estructuras-de-datos", "funciones", "Fundamentos", "modulos", "poo"]

# "for tree in carpetas" recorre cada elemento de la lista
# la variable receptora la he llamado "tree" porque representa un arbol de carpetas
# pero podria llamarse de cualquier forma
for tree in carpetas:
    print(tree)

# diferencia entre imprimir la lista completa vs imprimir elemento por elemento:
# print(carpetas)   muestra la lista con corchetes y comas
# print(tree)       muestra cada elemento en una línea separada

# o podria importar el módulo "os" que viene en python para obtener las carpetas 
# del sistema operativo

# carpetas = os.listdir(".")

# for tree in carpetas:
#      print(tree)

#-------------------------------------------------------------------------------------------------#
#----------------------------------------------WHILE----------------------------------------------#
#-------------------------------------------------------------------------------------------------#

# Con "WHILE" se repetira mientras la condicion sea verdadera, por lo que al final se le 
# entrega un dato para volverse falso asi no itera eternamente

x = 0
while x < len(carpetas):
    print(carpetas[x])
    x += 1

# contador = 0
# Variable que almacena el valor inicial, en este caso 0
# while contador < 5
# Condición que evalúa si contador es menor que 5. Mientras sea True ejecuta el bloque, cuando 
# sea falso se detiene.
# print(contador)
# Imprime el valor actual de contador en cada iteración.
# contador += 1
# aumenta el contador en 1 al contar. Sin esto la condición sería un loop infinito.

# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1

# Flujo completo
# 0 < 5 → True  → imprime 0 → contador = 1
# 1 < 5 → True  → imprime 1 → contador = 2
# 2 < 5 → True  → imprime 2 → contador = 3
# 3 < 5 → True  → imprime 3 → contador = 4
# 4 < 5 → True  → imprime 4 → contador = 5
# 5 < 5 → False → se detiene