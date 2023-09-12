import os
import shutil
import random

# Función para cambiar letras y dígitos
def modificar_archivo(ruta_archivo):
    with open(ruta_archivo, "r") as rt_arch: #read
        contenido = rt_arch.read()
        # Reemplazar letras y dígitos
        nuevos_caracteres = []
        for c in contenido:
            if c.isalpha():
                # Generar dígito aleatorio
                nuevos_c = random.choice("0123456789")
                nuevos_caracteres.append(nuevos_c)
            elif c.isdigit():
                # Generar letra aleatoria
                nuevos_c = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                nuevos_caracteres.append(nuevos_c)
            else:
                nuevos_caracteres.append(c)
        nuevo_contenido = "".join(nuevos_caracteres)
    with open(ruta_archivo, "w") as rt_arch: #write
        rt_arch.write(nuevo_contenido)

# Función para procesar archivo
def proceso(ruta_archivo, ruta_carpeta_origen, ruta_carpeta_destino):

    # Generar una nueva ruta para la copia del archivo
    ruta_relativa = os.path.relpath(ruta_archivo, ruta_carpeta_origen)
    nueva_ruta_archivo = os.path.join(ruta_carpeta_destino, ruta_relativa)

    # Crear la carpeta para la copia si no existe
    nueva_carpeta = os.path.dirname(nueva_ruta_archivo)
    if not os.path.exists(nueva_carpeta):
        os.makedirs(nueva_carpeta)

    # Copiar archivo a nueva ruta
    shutil.copy(ruta_archivo, nueva_ruta_archivo)

    # Modificar archivo copiado
    modificar_archivo(nueva_ruta_archivo)

    print(f"Archivo procesado: {nueva_ruta_archivo}")

ruta_carpeta_origen = "C:/Users/seren/Desktop/Practica_02/Sistemas"
ruta_carpeta_destino = "C:/Users/seren/Desktop/Practica_02/Sistemas_Copia"  # Cambia esto a la ruta de destino deseada
for raiz, direcciones, archivos in os.walk(ruta_carpeta_origen):
    for archivo in archivos:
        ruta_archivo = os.path.join(raiz, archivo)
        proceso(ruta_archivo, ruta_carpeta_origen, ruta_carpeta_destino)
