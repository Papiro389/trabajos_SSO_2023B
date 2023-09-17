def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as nom_arch:
        lineas = nom_arch.readlines()
    procesos = []
    for linea in lineas:
        nombre, tiempo, prioridad = linea.strip().split(',')
        proceso = {'Nombre': nombre, 'Tiempo': int(tiempo), 'Prioridad': int(prioridad)}
        procesos.append(proceso)
    return procesos

nombre_archivo = 'C:/Users/seren/Desktop/Practica_03-main/procesos.txt'
procesos = leer_archivo(nombre_archivo)

def round_robin(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    quantum = 3
    proceso_actual = 0
    while procesos_restantes > 0:
        proceso = procesos[proceso_actual]
        if proceso["Tiempo"] > 0:
            print(f"{proceso['Nombre']} corriendo por {min(quantum, proceso['Tiempo'])} segundos...")
            tiempo_ejecucion = min(quantum, proceso['Tiempo'])
            proceso["Tiempo"] -= tiempo_ejecucion
            tiempo_transcurrido += tiempo_ejecucion
            if proceso["Tiempo"] == 0:
                procesos_restantes -= 1
                procesos.pop(proceso_actual)
                if proceso_actual == len(procesos):
                    proceso_actual = 0
            else:
                proceso_actual = (proceso_actual + 1) % len(procesos)
        else:
            procesos_restantes -= 1
            procesos.pop(proceso_actual)
            if proceso_actual == len(procesos):
                proceso_actual = 0
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos") 

def sjf(procesos):
    tiempo_transcurrido = 0
    procesos_ordenados = sorted(procesos, key=lambda p: p["Tiempo"])
    for proceso in procesos_ordenados:
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

def fifo(procesos):
    tiempo_transcurrido = 0
    for proceso in procesos:
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

def prioridad(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    while procesos_restantes > 0:
        procesos = sorted(procesos, key=lambda x: x['Prioridad'])
        proceso = procesos[0]
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        tiempo_transcurrido += proceso['Tiempo']
        procesos_restantes -= 1
        procesos.pop(0)
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

def mostrar_menu():
    print("Selecciona un algoritmo de planificación de procesos:")
    print("1. SJF (Shortest Job First)")
    print("2. FIFO (First-In, First-Out)")
    print("3. Prioridades")
    print("4. Round Robin")
    print("5. Salir")

    eleccion = input("Ingresa el número de tu elección: ")
    return eleccion

def ejecutar_programa(procesos):
    while True:
        eleccion = mostrar_menu()
        
        if eleccion == "1":
            print("Corriendo algoritmo SJF:")
            sjf(procesos)
        elif eleccion == "2":
            print("Corriendo algoritmo FIFO:")
            fifo(procesos)
        elif eleccion == "3":
            print("Corriendo algoritmo Prioridades:")
            prioridad(procesos)
        elif eleccion == "4":
            print("Corriendo algoritmo Round Robin:")
            round_robin(procesos)
        elif eleccion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida del menú.")

ejecutar_programa(procesos)
