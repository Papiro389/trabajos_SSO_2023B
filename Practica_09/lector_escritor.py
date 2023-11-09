import tkinter as tk
import threading
import time
from threading import Semaphore

class Archivo:
    def __init__(self):
        self.archivo = open('archivo.txt', 'w+')
        self.semaforo = Semaphore(1)

    def leer(self):
        self.semaforo.acquire()
        self.archivo.seek(0)
        contenido = self.archivo.read()
        time.sleep(0.1)  # Simular delay de lectura
        self.semaforo.release()
        return contenido

    def editar(self, texto):
        self.semaforo.acquire()
        self.archivo.write(texto)
        self.semaforo.release()

    def guardar(self):
        self.archivo.close()
        self.archivo = open('archivo.txt', 'w+')

class Interfaz:
    def __init__(self, root, archivo):
        self.root = root
        self.archivo = archivo
        self.textbox = tk.Text(self.root, height=10, width=30)  # Especificar dimensiones
        self.textbox.pack()
        self.boton_leer = tk.Button(self.root, text='Leer', command=self.leer)
        self.boton_leer.pack()
        self.boton_editar = tk.Button(self.root, text='Editar', command=self.editar)
        self.boton_editar.pack()
        self.boton_guardar = tk.Button(self.root, text='Guardar', command=self.guardar)
        self.boton_guardar.pack()

    def leer(self):
        contenido = self.archivo.leer()
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('end', contenido)

    def editar(self):
        texto = self.textbox.get('1.0', 'end')
        self.archivo.editar(texto)

    def guardar(self):
        texto = self.textbox.get('1.0', 'end')
        self.archivo.editar(texto)
        self.archivo.guardar()

archivo = Archivo()

root1 = tk.Tk()
interfaz1 = Interfaz(root1, archivo)

root2 = tk.Tk()
interfaz2 = Interfaz(root2, archivo)

root3 = tk.Tk()
interfaz3 = Interfaz(root3, archivo)

tk.mainloop()
