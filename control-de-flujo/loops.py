# importacion siempre arriba
# import os

#------------------------------------------------------------------------------------------------#
#-----------------------------------------------FOR----------------------------------------------#
#------------------------------------------------------------------------------------------------#

# "for" itera sobre una secuencia de elementos uno por uno
# en cada vuelta toma un elemento, lo guarda en la variable y ejecuta
# el "for" tiene 4 formas comunes:
#  Numérica          for n in range(x)
#  Lista             for tree in carpetas
#  Con índice        for i, tree in enumerate(carpetas)
#  Dos listas        for a, b in zip(lista1, lista2)

#------------------------------------------------------------------------------------------------#
# FOR con RANGO numerico
# "for"         inicia el loop
# "n"           es la variable que recibe cada valor de la secuencia
# "in"          indica dentro de que va a iterar
# "range(4)"    genera la secuencia 0, 1, 2, 3
# se comienza desde 0 por lo que range(4) imprimira del 0 al 3
# "print(n)"    imprime el valor actual de n en cada iteración
print("FOR con RANGO")

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
# print(n, end="x")   cualquier cosa
# print(n, end="")    todo junto
# print(n, end="\n")  comportamiento por defecto

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# FOR con LISTA
# "for tree in carpetas"    recorre cada elemento de la lista
# "tree"                    variable receptora, puede llamarse de cualquier forma
# "carpetas"                lista de elementos a recorrer
# "print(tree)"             imprime el valor actual de tree en cada iteración
print("FOR con LISTA")

carpetas = ["C:\\", "control-de-flujo", "estructuras-de-datos", "funciones", "Fundamentos", "modulos", "poo"]

for tree in carpetas:
    print(tree)

# Flujo completo
# vuelta 1 → tree = "C:\\"                  → imprime "C:\\"
# vuelta 2 → tree = "control-de-flujo"      → imprime "control-de-flujo"
# vuelta 3 → tree = "estructuras-de-datos"  → imprime "estructuras-de-datos"
# no hay mas elementos → se detiene

# con os.listdir() se puede obtener las carpetas del sistema operativo
# carpetas = os.listdir(".")
# for tree in carpetas:
#     print(tree)

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# FOR con INDICE
# "for i, tree in enumerate(carpetas)"  recorre la lista enumerando cada elemento con índice
# "i"                                   es el índice o posición del elemento
# "tree"                                es el valor del elemento
# "enumerate"                           genera pares (índice, valor) automáticamente
print("FOR con INDICE")

for i, tree in enumerate(carpetas):
    print(i, tree)

# Flujo completo
# vuelta 1 → i = 0, tree = "C:\\"                  → imprime "0 C:\\"
# vuelta 2 → i = 1, tree = "control-de-flujo"      → imprime "1 control-de-flujo"
# vuelta 3 → i = 2, tree = "estructuras-de-datos"  → imprime "2 estructuras-de-datos"
# no hay mas elementos → se detiene

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# FOR con ZIP / MULTIPLES LISTAS
# "for numero, tree, letra in zip(numeros, carpetas, letras)"  recorre multiples listas a la vez
# "numero"      recibe cada elemento de la lista numeros
# "tree"        recibe cada elemento de la lista carpetas
# "letra"       recibe cada elemento de la lista letras
# "zip"         une las listas en pares, se detiene cuando la lista mas corta se acaba
print("FOR con ZIP / MULTIPLES LISTAS")

numeros = [1, 2, 3, 4, 5, 6, 7]
letras  = ["a", "b", "c", "d", "e", "f", "g", "h"]

for numero, tree, letra in zip(numeros, carpetas, letras):
    print(letra, numero, tree)

# Flujo completo
# vuelta 1 → numero = 1, tree = "C:\\",                 letra = "a" → imprime "a 1 C:\\"
# vuelta 2 → numero = 2, tree = "control-de-flujo",     letra = "b" → imprime "b 2 control-de-flujo"
# vuelta 3 → numero = 3, tree = "estructuras-de-datos", letra = "c" → imprime "c 3 estructuras-de-datos"
# no hay mas elementos → se detiene

print("#------------------------------------------------------------------------------------#")

#------------------------------------------------------------------------------------------------#
#----------------------------------------------WHILE---------------------------------------------#
#------------------------------------------------------------------------------------------------#

# "while" repite un bloque mientras la condicion sea verdadera
# el "while" tiene 3 formas comunes:
#  Numérica          while contador < 5
#  Con lista         while x < len(carpetas)
#  Infinito          while True

#------------------------------------------------------------------------------------------------#
# WHILE con CONTADOR
# "contador = 0"        variable que almacena el valor inicial
# "while contador < 5"  condicion que evalua si contador es menor que 5
# "print(contador)"     imprime el valor actual de contador en cada iteración
# "contador += 1"       incrementa contador en 1, sin esto seria un loop infinito
print("WHILE con CONTADOR")

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Flujo completo
# 0 < 5 → True  → imprime 0 → contador = 1
# 1 < 5 → True  → imprime 1 → contador = 2
# 2 < 5 → True  → imprime 2 → contador = 3
# 3 < 5 → True  → imprime 3 → contador = 4
# 4 < 5 → True  → imprime 4 → contador = 5
# 5 < 5 → False → se detiene

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# WHILE con LISTA
# "x = 0"                   indice inicial para acceder a los elementos
# "while x < len(carpetas)" recorre la lista mientras queden elementos
# "len(carpetas)"           devuelve el total de elementos de la lista, en este caso 7
# "carpetas[x]"             accede al elemento en la posición x
# "x += 1"                  incrementa x en 1, sin esto seria un loop infinito
print("WHILE con LISTA")

x = 0
while x < len(carpetas):
    print(carpetas[x])
    x += 1

# Flujo completo
# x = 0 → 0 < 7 → True  → imprime "C:\\"                 → x = 1
# x = 1 → 1 < 7 → True  → imprime "control-de-flujo"     → x = 2
# x = 2 → 2 < 7 → True  → imprime "estructuras-de-datos" → x = 3
# x = 7 → 7 < 7 → False → se detiene

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# WHILE con TRUE y BREAK
# "while True"              repite para siempre hasta que un "break" lo detenga
# "respuesta"               variable que guarda lo que el usuario escribe
# "input()"                 detiene el programa y espera que el usuario escriba algo
# "if respuesta == 'si'"    evalua si el usuario escribio exactamente "si"
# "break"                   si la condicion se cumple, sale del loop inmediatamente
# "bucle continua..."       si el usuario no escribe "si" el loop sigue
print("WHILE con TRUE y BREAK")

while True:
    respuesta = input("Que el bucle termine? : ")
    if respuesta == "si":
        break
    print("bucle continua...")

# Flujo completo
# vuelta 1 → usuario escribe "no"  → imprime "bucle continua..." → repite
# vuelta 2 → usuario escribe "no"  → imprime "bucle continua..." → repite
# vuelta 3 → usuario escribe "si"  → break → se detiene

print("#------------------------------------------------------------------------------------#")

#------------------------------------------------------------------------------------------------#
#------------------------------------MODIFICADORES-----------------------------------------------#
#------------------------------------------------------------------------------------------------#

# Los modificadores controlan el flujo dentro del loop
# se pueden usar en "for" y "while"
# exiten 4 modificadores:
#  break       sale del loop inmediatamente
#  continue    salta la iteración actual y continua con la siguiente
#  pass        no hace nada, es un placeholder
#  else        se ejecuta cuando el loop termina sin break

#------------------------------------------------------------------------------------------------#
# BREAK
# "break"       interrumpe el loop inmediatamente al cumplirse la condición
# "if n == 5"   cuando n vale 5 se ejecuta el break
# el loop no llega a imprimir el 5 porque break actúa antes del print
print("Modificador BREAK")

for n in range(10):
    if n == 5:
        break
    print(n)

# Flujo completo
# n = 0 → 0 != 5 → imprime 0
# n = 1 → 1 != 5 → imprime 1
# n = 4 → 4 != 5 → imprime 4
# n = 5 → 5 == 5 → break → se detiene

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# CONTINUE
# "continue"    salta la iteración actual y pasa a la siguiente
# "if n == 5"   cuando n vale 5 se ejecuta el continue
# el loop no imprime el 5 pero sigue con el 6, 7, 8, 9
print("Modificador CONTINUE")

for n in range(10):
    if n == 5:
        continue
    print(n)

# Flujo completo
# n = 4 → 4 != 5 → imprime 4
# n = 5 → 5 == 5 → continue → salta al siguiente
# n = 6 → 6 != 5 → imprime 6

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# PASS
# "pass"        no hace nada, es un marcador de posición
# "if n == 3"   cuando n vale 3 ejecuta pass, que no hace nada
# el loop imprime todos los números incluyendo el 3
print("Modificador PASS")

for n in range(5):
    if n == 3:
        pass
    print(n)

# Flujo completo
# n = 2 → imprime 2
# n = 3 → pass → no hace nada → imprime 3 igual
# n = 4 → imprime 4

print("#------------------------------------------------------------------------------------#")
#------------------------------------------------------------------------------------------------#
# ELSE
# "else" se ejecuta cuando el loop termina sin un break
# si hay un break el else NO se ejecut
print("Modificador ELSE sin break")

for n in range(5):
    print(n)
else:
    print("el loop termino normalmente")

print("Modificador ELSE con break")

for n in range(5):
    if n == 3:
        break
else:
    print("esto NO se imprime porque hubo un break")

# Flujo completo
# sin break → loop termina normalmente → else se ejecuta
# con break → loop se interrumpe       → else NO se ejecuta

print("#------------------------------------------------------------------------------------#")