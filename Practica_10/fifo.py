class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad


def simulacion_FIFO(archivo):
    cola_procesos = []
    with open(archivo, 'r') as f:
        for linea in f:
            datos = linea.strip().split(', ')
            nombre = datos[0]
            tiempo_ejecucion = int(datos[1])
            prioridad = int(datos[2])
            proceso = Proceso(nombre, tiempo_ejecucion, prioridad)
            cola_procesos.append(proceso)

    tiempo_total = 0
    while cola_procesos:
        proceso_actual = cola_procesos.pop(0)
        tiempo_total += proceso_actual.tiempo_ejecucion
        print(
            f"Proceso: {proceso_actual.nombre}, Tiempo de Ejecución: {proceso_actual.tiempo_ejecucion}, Prioridad: {proceso_actual.prioridad}")

    print(f"Tiempo total de ejecución: {tiempo_total}")


