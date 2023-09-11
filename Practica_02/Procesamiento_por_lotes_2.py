import os
import shutil
import random
import string

# Función para cambiar letras a dígitos aleatorios
def letras_a_digitos(texto):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            resultado += str(random.randint(0, 9))
        else:
            resultado += caracter
    return resultado

# Función para cambiar dígitos a letras aleatorias
def digitos_a_letras(texto):
    resultado = ""
    for caracter in texto:
        if caracter.isdigit():
            resultado += random.choice(string.ascii_uppercase)
        else:
            resultado += caracter
    return resultado

# Función para procesar un archivo
def procesar_archivo(archivo):
    with open(archivo, 'r') as file:
        contenido_original = file.read()

    contenido_modificado = letras_a_digitos(contenido_original)
    contenido_modificado = digitos_a_letras(contenido_modificado)

    # Crear una copia del archivo original con un sufijo "_modificado"
    nombre_archivo, extension = os.path.splitext(archivo)
    archivo_modificado = nombre_archivo + "_modificado" + extension

    with open(archivo_modificado, 'w') as file:
        file.write(contenido_modificado)

# Función para procesar todos los archivos en una carpeta y subcarpetas
def procesar_carpeta(carpeta):
    for dirpath, dirnames, filenames in os.walk(carpeta):
        for filename in filenames:
            archivo = os.path.join(dirpath, filename)
            procesar_archivo(archivo)

# Ruta de la carpeta que deseas procesar
carpeta_entrada = "C:/Users/seren/Desktop/Practica_02-main/Sistemas"
carpeta_salida = "C:/Users/seren/Desktop/Practica_02-main/Sistemas_copy"

# Verifica si la carpeta de salida ya existe y elimínala si es necesario
if os.path.exists(carpeta_salida):
    shutil.rmtree(carpeta_salida)

# Copia la carpeta de entrada a la carpeta de salida
shutil.copytree(carpeta_entrada, carpeta_salida)

# Procesa los archivos en la carpeta de salida
procesar_carpeta(carpeta_salida)

print("Proceso completado.")
