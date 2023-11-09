import tkinter as tk
import threading
import os
import time
from tkinter import messagebox

# Semáforos para el algoritmo lector-escritor
lectores = 0
escritores = 0
mutex = threading.Semaphore(1)
db = threading.Semaphore(1)
editando = [False, False, False]


def leer_texto(textbox):
    global lectores
    with mutex:
        lectores += 1
        if lectores == 1:
            db.acquire()
    contenido = ""
    with open("texto.txt", "r") as file:
        contenido = file.read()
    for letra in contenido:
        textbox.insert(tk.END, letra)
        time.sleep(0.05)  # Añadir un pequeño delay por letra
        textbox.update()
    with mutex:
        lectores -= 1
        if lectores == 0:
            db.release()



# Función para simular escritura
def editar_texto(textbox, content):
    global escritores
    with db:
        escritores += 1
        if escritores == 1:
            mutex.acquire()
    with open("texto.txt", "w") as file:
        file.write(content)
    with db:
        escritores -= 1
        if escritores == 0:
            mutex.release()


# Función para manejar el botón "Leer"
def leer_handler(textbox):
    threading.Thread(target=lambda: leer_texto(textbox)).start()


# Función para manejar el botón "Guardar"
def guardar_handler(textbox):
    content = textbox.get("1.0", tk.END)
    threading.Thread(target=lambda: editar_texto(textbox, content)).start()


# Función para manejar el botón "Editar"
def editar_handler(index):
    global editando
    editando[index] = not editando[index]
    if editando[index]:
        for i, boton_editar in enumerate(botones_editar):
            if i != index:
                boton_editar.config(state=tk.DISABLED)  # Bloquear los demás botones "Editar"
        for boton_leer in botones_leer:
            boton_leer.config(state=tk.DISABLED)  # Bloquear los botones "Leer"
        for boton_guardar in botones_guardar:
            boton_guardar.config(state=tk.DISABLED)  # Bloquear los botones "Guardar"
    else:
        for boton_editar in botones_editar:
            boton_editar.config(state=tk.NORMAL)  # Desbloquear todos los botones "Editar"
        for boton_leer in botones_leer:
            boton_leer.config(state=tk.NORMAL)  # Desbloquear los botones "Leer"
        for boton_guardar in botones_guardar:
            boton_guardar.config(state=tk.NORMAL)  # Desbloquear los botones "Guardar"


# Función para manejar el botón "Limpiar"
def limpiar_handler(textbox):
    textbox.delete("1.0", tk.END)


# Función para crear la interfaz gráfica
def crear_interfaz():
    root = tk.Tk()
    root.title("Lector - Escritor")

    global botones_editar, botones_leer, botones_guardar

    # Primera área de texto y botones
    frame1 = tk.Frame(root)
    frame1.pack(side=tk.LEFT)
    textbox1 = tk.Text(frame1, height=10, width=50)
    textbox1.pack()
    boton_leer1 = tk.Button(frame1, text="Leer", command=lambda: leer_handler(textbox1))
    boton_leer1.pack()
    boton_editar1 = tk.Button(frame1, text="Editar", command=lambda: editar_handler(0))
    boton_editar1.pack()
    boton_guardar1 = tk.Button(frame1, text="Guardar", command=lambda: guardar_handler(textbox1))
    boton_guardar1.pack()
    boton_limpiar1 = tk.Button(frame1, text="Limpiar Pantalla", command=lambda: limpiar_handler(textbox1))
    boton_limpiar1.pack()

    # Segunda área de texto y botones
    frame2 = tk.Frame(root)
    frame2.pack(side=tk.LEFT)
    textbox2 = tk.Text(frame2, height=10, width=50)
    textbox2.pack()
    boton_leer2 = tk.Button(frame2, text="Leer", command=lambda: leer_handler(textbox2))
    boton_leer2.pack()
    boton_editar2 = tk.Button(frame2, text="Editar", command=lambda: editar_handler(1))
    boton_editar2.pack()
    boton_guardar2 = tk.Button(frame2, text="Guardar", command=lambda: guardar_handler(textbox2))
    boton_guardar2.pack()
    boton_limpiar2 = tk.Button(frame2, text="Limpiar Pantalla", command=lambda: limpiar_handler(textbox2))
    boton_limpiar2.pack()

    # Tercera área de texto y botones
    frame3 = tk.Frame(root)
    frame3.pack(side=tk.LEFT)
    textbox3 = tk.Text(frame3, height=10, width=50)
    textbox3.pack()
    boton_leer3 = tk.Button(frame3, text="Leer", command=lambda: leer_handler(textbox3))
    boton_leer3.pack()
    boton_editar3 = tk.Button(frame3, text="Editar", command=lambda: editar_handler(2))
    boton_editar3.pack()
    boton_guardar3 = tk.Button(frame3, text="Guardar", command=lambda: guardar_handler(textbox3))
    boton_guardar3.pack()
    boton_limpiar3 = tk.Button(frame3, text="Limpiar Pantalla", command=lambda: limpiar_handler(textbox3))
    boton_limpiar3.pack()

    botones_editar = [boton_editar1, boton_editar2, boton_editar3]
    botones_leer = [boton_leer1, boton_leer2, boton_leer3]
    botones_guardar = [boton_guardar1, boton_guardar2, boton_guardar3]

    root.mainloop()




# Verificar y crear el archivo si no existe
if not os.path.exists("archivo.txt"):
    with open("archivo.txt", "w") as file:
        file.write("escribe algo: ")

# Iniciar la interfaz gráfica
crear_interfaz()
