import os

lista_Archivos = []

def mejor_Ajuste(tamano_Proceso, espacio_Memoria, procesos_Memoria, estado_Memoria):    #Funcion del algoritmo del mejor ajuste
    mejor_Ajuste_Idx = -1
    espacio_Libre = float('inf')

    for i in range(len(espacio_Memoria)):
        if espacio_Memoria[i] >= tamano_Proceso and estado_Memoria[i] == 'disponible' and espacio_Memoria[i] - tamano_Proceso < espacio_Libre:
            mejor_Ajuste_Idx = i
            espacio_Libre = espacio_Memoria[i] - tamano_Proceso

    if mejor_Ajuste_Idx != -1:
        procesos_Memoria.append(tamano_Proceso)
        espacio_Memoria[mejor_Ajuste_Idx] -= tamano_Proceso
        print(f"Proceso de {tamano_Proceso} KB asignado al espacio {mejor_Ajuste_Idx}")
    else:
        print(f"Proceso {proceso}: Tamaño {tamano_Proceso} KB no hay suficiente espacio en la memoria")

def primer_Ajuste(tamano_Proceso, espacios_Memoria, estado_Memoria):    #Funcion del algoritmo del primer ajuste
    for i in range(len(espacios_Memoria)):
        if espacios_Memoria[i] >= tamano_Proceso and estado_Memoria[i] == 'disponible':
            print(f"Proceso de {tamano_Proceso} KB asignado al espacio {i}")
            espacios_Memoria[i] -= tamano_Proceso
            return True
    return False

def peor_Ajuste(espacios_Memoria, tamano_Proceso, estado_Memoria):  #Funcion del algoritmo del peor ajuste
    for proceso in tamano_Proceso:
        peor_Ajuste_Index = -1
        peor_Ajuste_Tamano = -1

        for i in range(len(espacios_Memoria)):
            if espacios_Memoria[i] >= proceso[1] and estado_Memoria[i] == 'disponible':
                if peor_Ajuste_Index == -1 or espacios_Memoria[i] > espacios_Memoria[peor_Ajuste_Index]:
                    peor_Ajuste_Index = i
                    peor_Ajuste_Tamano = espacios_Memoria[i]

        if peor_Ajuste_Index != -1:
            espacios_Memoria[peor_Ajuste_Index] -= proceso[1]
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"Proceso de {proceso[1]} KB asignado en el espacio {peor_Ajuste_Index}")
        else:
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"Proceso {proceso[0]}: Tamaño {proceso[1]} KB no hay suficiente espacio en la memoria")

def siguiente_Ajuste(espacios_Memoria, tamano_Proceso, estado_Memoria): #Funcion del algoritmo del siguiente ajuste
    ultimo_Indice_Asignado = 0

    for proceso in tamano_Proceso:
        proceso_Asignado = False

        for i in range(ultimo_Indice_Asignado, len(espacios_Memoria)):
            if espacios_Memoria[i] >= proceso[1] and estado_Memoria[i] == 'disponible':
                espacios_Memoria[i] -= proceso[1]
                print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
                print(f"Proceso de {proceso[1]} KB asignado en el espacio {i}")
                proceso_Asignado = True
                ultimo_Indice_Asignado = i + 1
                break

        if not proceso_Asignado:
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"No se pudo asignar el proceso {proceso[0]} de {proceso[1]} KB")

def agregar_Espacio_Memoria(espacio_Memoria, estado_Memoria):
    tamano = int(input("Ingrese el tamaño del nuevo espacio de memoria en KB: "))
    estado = input("Ingrese el estado del nuevo espacio de memoria (disponible/ocupado): ")
    ubicacion = input("Ingrese la ubicación del nuevo espacio de memoria (inicio/final): ").lower()

    if ubicacion == "inicio":
        espacio_Memoria.insert(0, tamano)
        estado_Memoria.insert(0, estado)
    elif ubicacion == "final":
        espacio_Memoria.append(tamano)
        estado_Memoria.append(estado)
    else:
        print("Ubicación no válida. El espacio de memoria no se ha agregado.")

    print(f"Espacio de memoria de {tamano} KB con estado '{estado}' agregado con éxito en la ubicación {ubicacion}.")

def imprimir_Estado_Memoria(espacio_Memoria, estado_Memoria):
    print("\nEstado actual de la memoria:\n")
    for i in range(len(espacio_Memoria)):
        if espacio_Memoria[i] == 0:
            estado_Memoria[i] = 'ocupado'
        print(f"Espacio {i}: {espacio_Memoria[i]} KB ({estado_Memoria[i]})")

def cargar_Archivos(nombre_Archivo):
    procesos_en_Memoria = []

    with open(nombre_Archivo, "r") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        proceso, tamano = linea.strip().split(', ')
        tamano_Proceso = int(tamano.rstrip('kb'))
        procesos_en_Memoria.append((proceso,int(tamano_Proceso)))

    return procesos_en_Memoria

def agregar_Archivos_Virtuales(lista_Archivos):
    nombre = input("Nombre del archivo: ")
    peso = int(input("Peso del archivo en KB: "))
    posicion = input("¿Desea agregar al inicio o al final?(P/A): ").strip().lower()

    nuevo_Archivo = (nombre, peso)
    lista_Archivos = cargar_Archivos(lista_de_Archivos)

    if posicion.lower() == "p":
        lista_Archivos.insert(0, nuevo_Archivo) #Agregar el nuevo proceso al principio de la lista global
    else:
        lista_Archivos.append(nuevo_Archivo)

    with open(lista_de_Archivos, "w") as archivo:    #Sobrescribir el archivo con la lista actualizada de procesos
        for proceso in lista_Archivos:
            archivo.write(f"{proceso[0]}, {proceso[1]}kb\n")

def agregar_Archivos_Fisicos(lista_Archivos):
    carpeta = os.path.dirname(os.path.abspath(__file__))

    nombre_Carpeta = input("\nIngrese el nombre de la carpeta o presione enter para usar la carpeta raiz: ")
    print("")

    ruta_Carpeta = os.path.join(carpeta, nombre_Carpeta)

    if os.path.isdir(ruta_Carpeta):
        archivos = os.listdir(ruta_Carpeta)
        print("\n\t",nombre_Carpeta,"\n")
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_Carpeta, archivo)
            
            if os.path.isfile(ruta_archivo):
                tamaño_bytes = os.path.getsize(ruta_archivo)
                tamaño_kb = tamaño_bytes / 1024
                print(f"Archivo: {archivo}, Tamaño en KB: {tamaño_kb:.2f} KB")

                respuesta = input("¿Desea agregar este archivo a la lista de archivos (S/N)? ").strip().lower()
                if respuesta == "s":
                    nuevo_Archivo = (archivo, int(tamaño_kb))
                    lista_Archivos.append(nuevo_Archivo)

        with open("archivos.txt", "a") as archivo:  # Abre el archivo en modo de agregado
            for proceso in lista_Archivos:
                archivo.write(f"{proceso[0]}, {proceso[1]}kb\n")
        print("Archivos agregados al archivo 'archivos.txt' con éxito.")

    else:
        print(f"{ruta_Carpeta} no es una carpeta válida.")

lista_de_Archivos = "archivos.txt"
#Espacios de memoria para los algoritmos
espacio_Memoria_original = [1000, 400, 1800, 700, 900, 1200, 1500]
estado_Memoria_original = ['disponible'] * len(espacio_Memoria_original)

espacio_Memoria1 = espacio_Memoria_original.copy()
estado_Memoria1 = estado_Memoria_original.copy()
espacio_Memoria2 = espacio_Memoria_original.copy()
estado_Memoria2 = estado_Memoria_original.copy()
espacio_Memoria3 = espacio_Memoria_original.copy()
estado_Memoria3 = estado_Memoria_original.copy()
espacio_Memoria4 = espacio_Memoria_original.copy()
estado_Memoria4 = estado_Memoria_original.copy()

#Menu del programa
while True:
    print("\n\tMenu\n")
    print("Selecciona un algoritmo de asignación de memoria:")
    print("1. Mejor Ajuste")
    print("2. Primer Ajuste")
    print("3. Peor Ajuste")
    print("4. Siguiente Ajuste")
    print("5. Agregar Espacio de Memoria")
    print("6. Ver Espacios de Memoria")
    print("7. Agregar nuevos archivos")
    print("8. Salir")

    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == '1':
        print("\n\tMejor Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso, tamano = linea.strip().split(', ')
            tamano_Proceso = int(tamano.rstrip('kb'))
            print(f"Procesando: {proceso} ({tamano_Proceso} KB)")
            mejor_Ajuste(tamano_Proceso, espacio_Memoria1, procesos_en_Memoria, estado_Memoria1)

        imprimir_Estado_Memoria(espacio_Memoria1, estado_Memoria1)

    elif opcion == '2':
        print("\n\tPrimer Ajuste\n")
        with open('archivos.txt', 'r') as file:
            lineas = file.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso, tamano = linea.strip().split(', ')
            tamano = int(tamano[:-2])
            procesos_en_Memoria.append((proceso, tamano))
            
        for proceso, tamano in procesos_en_Memoria:
            print(f"Procesando: {proceso} ({tamano} KB)")
            if not primer_Ajuste(tamano, espacio_Memoria2, estado_Memoria2):
                print(f"Proceso {proceso}: Tamaño {tamano} KB no hay suficiente espacio en la memoria")
        
        imprimir_Estado_Memoria(espacio_Memoria2, estado_Memoria2)

    elif opcion == '3':
        print("\n\tPeor Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso = linea.strip().split(", ")
            nombre_Proceso = proceso[0]
            tamano_Proceso = int(proceso[1].rstrip("kb"))
            procesos_en_Memoria.append((nombre_Proceso, tamano_Proceso))

        peor_Ajuste(espacio_Memoria3, procesos_en_Memoria, estado_Memoria3)

        imprimir_Estado_Memoria(espacio_Memoria3, estado_Memoria3)

    elif opcion == '4':
        print("\n\tSiguiente Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso = linea.strip().split(", ")
            nombre_Proceso = proceso[0]
            tamano_Proceso = int(proceso[1].rstrip("kb"))
            procesos_en_Memoria.append((nombre_Proceso, tamano_Proceso))

        siguiente_Ajuste(espacio_Memoria4, procesos_en_Memoria, estado_Memoria4)

        imprimir_Estado_Memoria(espacio_Memoria4, estado_Memoria4)

    elif opcion == '5':
        while True:
            print("\n\tAgregar Espacios de Memoria\n")
            print("1. Mejor Ajuste")
            print("2. Primer Ajuste")
            print("3. Peor Ajuste")
            print("4. Siguiente Ajuste")
            print("5. Salir")

            opcion = input("Ingresa el número de la opción deseada: ")
            if opcion == '1':
                print("\n\tMejor Ajuste\n")
                agregar_Espacio_Memoria(espacio_Memoria1, estado_Memoria1)
            elif opcion == '2':
                print("\n\tPrimer Ajuste\n")
                agregar_Espacio_Memoria(espacio_Memoria2, estado_Memoria2)
            elif opcion == '3':
                print("\n\tPeor Ajuste\n")
                agregar_Espacio_Memoria(espacio_Memoria3, estado_Memoria3)
            elif opcion == '4':
                print("\n\tSiguiente Ajuste\n")
                agregar_Espacio_Memoria(espacio_Memoria4, estado_Memoria4)
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

    elif opcion == '6':
        while True:
                print("\n\tVer Espacios de Memoria\n")
                print("1. Mejor Ajuste")
                print("2. Primer Ajuste")
                print("3. Peor Ajuste")
                print("4. Siguiente Ajuste")
                print("5. Salir")

                opcion = input("Ingresa el número de la opción deseada: ")
                if opcion == '1':
                    print("\n\tMejor Ajuste")
                    imprimir_Estado_Memoria(espacio_Memoria1, estado_Memoria1)
                elif opcion == '2':
                    print("\n\tPrimer Ajuste")
                    imprimir_Estado_Memoria(espacio_Memoria2, estado_Memoria2)
                elif opcion == '3':
                    print("\n\tPeor Ajuste")
                    imprimir_Estado_Memoria(espacio_Memoria3, estado_Memoria3)
                elif opcion == '4':
                    print("\n\tSiguiente Ajuste")
                    imprimir_Estado_Memoria(espacio_Memoria4, estado_Memoria4)
                elif opcion == '5':
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")
    
    elif opcion == '7':
        while True:
                print("\n\tAgregar nuevos Archivos\n")
                print("1. Fisicos")
                print("2. Virtuales")
                print("3. Salir")

                opcion = input("Ingresa el número de la opcion deseada: ")
                if opcion == '1':
                    print("\n\tAgregar archivos Fisicos")
                    agregar_Archivos_Fisicos(lista_Archivos)
                elif opcion == '2':
                    print("\n\tAgregar archivos Virtuales")
                    agregar_Archivos_Virtuales(lista_de_Archivos)
                elif opcion == '3':
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")

    elif opcion == '8':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
