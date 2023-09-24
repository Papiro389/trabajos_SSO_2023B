import os

def leer_archivos(nombre_archivo):
    archivos = []
    with open(nombre_archivo) as f:
        lines = f.readlines()
        for line in lines:
            nombre, tamano = line.strip().split(', ')
            archivos.append((nombre, int(tamano.replace('kb', ''))))
    return archivos

def primer_ajuste(memoria, archivos):
    for archivo in archivos:
        nombre, tamano = archivo
        asignado = False
        for i, segmento in enumerate(memoria):
            if segmento[1] - segmento[0] >= tamano:
                memoria[i] = (segmento[0], segmento[1] - tamano)
                asignado = True
                print(f'{nombre} asignado a segmento {i}')
                break
        if not asignado:
            print(f'{nombre} no pudo ser asignado')

def mejor_ajuste(memoria, archivos):
    for archivo in archivos:
        nombre, tamano = archivo
        mejor_segmento = None
        for segmento in memoria:
            if segmento[1] - segmento[0] >= tamano:
                if mejor_segmento is None or (segmento[1] - segmento[0]) < (mejor_segmento[1] - mejor_segmento[0]):
                    mejor_segmento = segmento
        if mejor_segmento is not None:
            i = memoria.index(mejor_segmento)
            memoria[i] = (mejor_segmento[0], mejor_segmento[1] - tamano)
            print(f'{nombre} asignado a segmento {i}')
        else:
            print(f'{nombre} no pudo ser asignado')

def peor_ajuste(memoria, archivos):
    for archivo in archivos:
        nombre, tamano = archivo
        peor_segmento = None
        for segmento in memoria:
            if segmento[1] - segmento[0] >= tamano:
                if peor_segmento is None or (segmento[1] - segmento[0]) > (peor_segmento[1] - peor_segmento[0]):
                    peor_segmento = segmento
        if peor_segmento is not None:
            i = memoria.index(peor_segmento)
            memoria[i] = (peor_segmento[0], peor_segmento[1] - tamano)
            print(f'{nombre} asignado a segmento {i}')
        else:
            print(f'{nombre} no pudo ser asignado')

def siguiente_ajuste(memoria, archivos):
    ultimo_segmento = 0
    for archivo in archivos:
        nombre, tamano = archivo
        asignado = False
        for i in range(ultimo_segmento, len(memoria)):
            segmento = memoria[i]
            if segmento[1] - segmento[0] >= tamano:
                memoria[i] = (segmento[0], segmento[1] - tamano)
                asignado = True
                ultimo_segmento = i
                print(f'{nombre} asignado a segmento {i}')
                break
        if not asignado:
            for i in range(ultimo_segmento):
                segmento = memoria[i]
                if segmento[1] - segmento[0] >= tamano:
                    memoria[i] = (segmento[0], segmento[1] - tamano)
                    asignado = True
                    ultimo_segmento = i
                    print(f'{nombre} asignado a segmento {i}')
                    break
        if not asignado:
            print(f'{nombre} no pudo ser asignado')

# Definición de la lista de segmentos de memoria
memoria = [(0, 1000), (0, 400), (0, 1800), (0, 700), (0, 900), (0, 1200), (0, 1500)]

# Leer archivos desde 'archivos.txt'
archivos = leer_archivos('archivos.txt')

while True:
    os.system('cls')
    print('\n')
    print('1. Primer ajuste')
    print('2. Mejor ajuste')
    print('3. Peor ajuste')
    print('4. Siguiente ajuste')
    print('5. Salir')
    print("\n")
    opcion = int(input('Escriba el número de la opción que desea utilizar: '))

    if opcion == 1:
        primer_ajuste(memoria, archivos)
    elif opcion == 2:
        mejor_ajuste(memoria, archivos)
    elif opcion == 3:
        peor_ajuste(memoria, archivos)
    elif opcion == 4:
        siguiente_ajuste(memoria, archivos)
    elif opcion == 5:
        break
    else:
        print('Opción inválida. Intente de nuevo.')

