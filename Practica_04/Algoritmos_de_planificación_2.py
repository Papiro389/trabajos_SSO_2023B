import os

#Funcion para procesar el archivo 
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as nom_arch:
        lineas = nom_arch.readlines()
    procesos = []
    for linea in lineas:
        nombre, tiempo, prioridad = linea.strip().split(',')
        proceso = {'Nombre': nombre, 'Tiempo': int(tiempo), 'Prioridad': int(prioridad)}
        procesos.append(proceso)

    return procesos

nombre_archivo = 'procesos.txt'
procesos = leer_archivo(nombre_archivo)

def agregar_proceso(procesos):
    nombre = input("Ingrese el nombre del proceso: ")
    tiempo = int(input("Ingrese el tiempo de duración del proceso: "))
    prioridad = int(input("Ingrese la prioridad del proceso: "))
    posicion = input("Ingrese la posición del proceso (al principio o al final): ")
    if posicion.lower() == "al principio":
        procesos.insert(0, {'Nombre': nombre, 'Tiempo': int(tiempo), 'Prioridad': int(prioridad)})
    else:
        procesos.append({'Nombre': nombre, 'Tiempo': int(tiempo), 'Prioridad': int(prioridad)})
    print(f"Proceso {nombre} agregado con éxito")

    # Guardar los procesos en el archivo
    with open(nombre_archivo, 'w') as nom_arch:
        for proceso in procesos:
            nom_arch.write(f"{proceso['Nombre']},{proceso['Tiempo']},{proceso['Prioridad']}\n")

#Funcion: algoritmo Round Robin
def round_robin(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    quantum = 3
    proceso_actual = 0
    #Selecciona el proceso actual 
    while procesos_restantes > 0:
        proceso = procesos[proceso_actual]
        #Verifica el proceso si tiene tiempo restante para ejecutarse 
        if proceso["Tiempo"] > 0:
            tiempo_restante = proceso["Tiempo"] - min(quantum, proceso['Tiempo'])
            if tiempo_restante > 0:
                print(f"{proceso['Nombre']} corriendo por {min(quantum, proceso['Tiempo'])} segundos... Falta {tiempo_restante} segundos para terminar")
            else:
                print(f"{proceso['Nombre']} corriendo por {min(quantum, proceso['Tiempo'])} segundos... Proceso finalizado")
            tiempo_ejecucion = min(quantum, proceso['Tiempo'])
            proceso["Tiempo"] -= tiempo_ejecucion
            tiempo_transcurrido += tiempo_ejecucion
            #Si el proceso termina durante este tiempo, disminuye contador de procesos restantes y se elimina
            if proceso["Tiempo"] == 0:
                procesos_restantes -= 1
                procesos.pop(proceso_actual)
                #Establece indice y continua con el siguiente proceso
                if proceso_actual == len(procesos):
                    proceso_actual = 0
            #Si no termina durante este tiempo, se mueve cola y continua con el siguiente proceso
            else:
                proceso_actual = (proceso_actual + 1) % len(procesos)
        #Si el proceso actual no tiene tiempo , disminuye contador y se elimina 
        else:
            procesos_restantes -= 1
            procesos.pop(proceso_actual)
            #Establece indice y continua con el siguiente proceso
            if proceso_actual == len(procesos):
                proceso_actual = 0
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion: algoritmo SJF
def sjf(procesos):
    tiempo_transcurrido = 0
    # Ordena los procesos en orden ascendente
    procesos_ordenados = sorted(procesos, key=lambda p: p["Tiempo"])
    for proceso in procesos_ordenados:
        print(f"{proceso['Nombre']} corriendo por ", end='')
        for t in range(proceso['Tiempo'], 0, -1):
            print(f"{t}, ", end='')
        print("0 segundos... Proceso finalizado")
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion: algoritmo FIFO
def fifo(procesos):
    tiempo_transcurrido = 0
    for proceso in procesos:
        print(f"{proceso['Nombre']} corriendo por ", end='')
        for t in range(proceso['Tiempo'], 0, -1):
            print(f"{t}, ", end='')
        print("0 segundos... Proceso finalizado")
        #Mide el tiempo total trancurrido de cada proceso 
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion: Prioridades
def prioridad(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    while procesos_restantes > 0:
        # Ordenar los procesos por prioridad de forma ascendente
        procesos = sorted(procesos, key=lambda x: x['Prioridad'])
        # Ejecutar el proceso con mayor prioridad
        proceso = procesos[0]
        # Construir la cadena del proceso con los segundos restantes
        proceso_str = f"{proceso['Nombre']} corriendo por "
        tiempo_restante = proceso['Tiempo']
        while tiempo_restante >= 0:
            proceso_str += str(tiempo_restante)
            if tiempo_restante > 0:
                proceso_str += ", "
            else:
                proceso_str += " segundos... Proceso finalizado"
            tiempo_restante -= 1
        print(proceso_str)
        #Mide el tiempo total trancurrido de cada proceso
        tiempo_transcurrido += proceso['Tiempo']
        procesos_restantes -= 1
        # Eliminar el proceso de la lista
        procesos.pop(0)
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#para agregar procesos
def menu(procesos):
    procesos = leer_archivo(nombre_archivo)
    os.system('cls')
    print("Bienvenido al menu, selecciona una opcion:")
    print("1. Agregar proceso")
    print("2. Regresar al menú")

    opcion = input("Ingrese una opción: ")
    print("\n")

    if opcion == "1":
       agregar_proceso(procesos)
       
    elif opcion == "2":
        menu_algoritmos(procesos)
    else:
        print("Opción inválida.")

    print("\n")
    input("Presione ENTER para continuar...")
    os.system('cls')
    menu(procesos)

    

def menu_algoritmos(procesos):
    procesos = leer_archivo(nombre_archivo)
    os.system('cls')
    print("Selecciona un algoritmo de planificación de procesos:")
    print("1. SJF (Shortest Job First)")
    print("2. FIFO (First-In, First-Out)")
    print("3. Prioridades")
    print("4. Round Robin")
    print("5. agregar procesos")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")
    print("\n")

    if opcion == "1":
        sjf(procesos)
    elif opcion == "2":
        fifo(procesos)
    elif opcion == "3":
        prioridad(procesos)
    elif opcion == "4":
        round_robin(procesos)
    elif opcion == "5":
        menu(procesos)
    elif opcion == "6":
        quit()
    else:
        print("Opción inválida. Intente de nuevo.")

    print("\n")

    input("Presione ENTER para continuar...")
    os.system('cls')
    menu_algoritmos(procesos)

menu_algoritmos(procesos)
