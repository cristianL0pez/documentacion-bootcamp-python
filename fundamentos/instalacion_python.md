## GUÍA DE INSTALACIÓN DE PYTHON
Autor: Karen Ñanco Vásquez
Fecha: 15-03-2026
Issue relacionada: #60

# 📘 Definición
La instalación de Python es el proceso de incorporar el intérprete del lenguaje en tu sistema operativo. El intérprete es el programa que "traduce" el código que escribes en archivos .py a un lenguaje que tu procesador puede entender y ejecutar.

Para instalarlo, generalmente descargamos un paquete que incluye:

1. El motor de Python.
2. pip (el gestor para instalar librerías).
3. IDLE (un editor básico para pruebas rápidas).

# 🧠 ¿Para qué sirve?
Sin el intérprete instalado localmente, no puedes ejecutar programas de Python en tu propia máquina. Es fundamental porque:

1. Permite el desarrollo profesional: Los entornos en la nube (como Google Colab) son útiles, pero el software real se construye y despliega desde entornos locales.
2. Gestión de librerías: Te permite usar pip para descargar herramientas de terceros (Pandas, Flask, Pygame).
3. Automatización de sistema: Puedes crear scripts que organicen tus archivos, envíen correos o procesen datos de tu disco duro.

# 🛠️ Pasos para Instalar

En *Windows*
1. Ve a python.org.
2. Descarga el instalador para Windows (ej. Python 3.12.x).
3. ¡CRÍTICO!: Al abrir el instalador, marca la casilla que dice "Add Python to PATH". Si no lo haces, no podrás usar el comando python en la terminal.
4. Haz clic en "Install Now".

En *macOS / Linux*
macOS: Puedes usar el instalador de la web oficial o usar Homebrew con el comando brew install python.

Linux: Normalmente ya viene instalado. Si no, usa tu gestor de paquetes (ej. sudo apt install python3).

# 🧩 Sintaxis
Una vez instalado, la "sintaxis" para interactuar con Python desde la consola y verificar que todo esté en orden es la siguiente:

# Verificar la instalación en la terminal (PowerShell, CMD o Bash)
python --version

# Si en Mac/Linux el anterior falla, intenta con:
python3 --version

# Ejecutar el modo interactivo (REPL)
python

# Dentro de Python, prueba este comando:
>>> print("Hola desde mi propia computadora")

# Para salir del modo interactivo:
>>> exit()

