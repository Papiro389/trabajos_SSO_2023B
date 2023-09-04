# Función para convertir de decimal a hexadecimal
def decimal_hexadecimal(num_dec):
    return hex(num_dec)[2:].upper()

# Función para procesar una línea de texto
def proceso(linea):
    cadenas = linea.strip().split(',')

    # resultado segunda_cadena
    segunda_cadena = cadenas[2].strip()
    
    # Obtener la dirección IP y convertirla a hexadecimal
    direccion_ip = cadenas[-1].strip()
    partes_ip = direccion_ip.split('.')

    # resultado dirección hex
    direccion_hexadecimal = '.'.join([decimal_hexadecimal(int(partes)) for partes in partes_ip])

    # Obtener los números en decimal
    numeros_decimales = [str(int(x, 16)) for x in cadenas[0].split('/')[0].split(':')]

    # imprime el resultado
    resultado = f"{segunda_cadena} : {' : '.join(numeros_decimales)} : {direccion_hexadecimal}\n"
    return resultado

# dirección de los archivos
entrada = "D:/VSC/SSO/practica_01/prueba2.txt"
salida = "D:/VSC/SSO/practica_01/salida.txt"

try:
    archivo_entrada = open(entrada, 'r')
    archivo_salida = open(salida, 'w')

    for linea in archivo_entrada:
        archivo_salida.write(proceso(linea))

    archivo_entrada.close()
    archivo_salida.close()

    print("Proceso completado con éxito. Los resultados se han guardado en 'salida.txt'")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")
