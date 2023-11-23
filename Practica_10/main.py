import tkinter as tk
import sys
# from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring, askinteger
import threading
import fifo
import prioridades
import rr
import sjf
import os


class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad


class Aplicacion:

    def limpiar_consola(self):
        # Verificamos el sistema operativo para utilizar el comando adecuado
        if sys.platform.startswith('win'):
            os.system('cls')
            self.consola.delete('1.0', tk.END)
        else:
            os.system('clear')


    def __init__(self, root):
        self.root = root
        self.root.title("Planificador de Procesos")

        # Variable para controlar el estado del hilo de procesos
        self.ejecucion_procesos = False

        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear etiqueta de título
        

        # Crear consola
        self.consola = tk.Text(self.root, height=10, width=50)
        self.consola.grid(row=1, column=0, columnspan=3, pady=10)

        # Crear botones
        btn_fifo = tk.Button(self.root, text="FIFO", command=self.ejecutar_fifo, height=2, width=20,bg="lightblue", fg="darkblue")
        btn_fifo.grid(row=2, column=0, padx=10, pady=5)

        btn_prioridades = tk.Button(self.root, text="Prioridades", command=self.ejecutar_prioridades, height=2, width=20,bg="lightblue", fg="darkblue")
        btn_prioridades.grid(row=2, column=1, padx=10, pady=5)

        btn_rr = tk.Button(self.root, text="Round Robin", command=self.ejecutar_rr, height=2, width=20,bg="lightblue", fg="darkblue")
        btn_rr.grid(row=3, column=0, padx=10, pady=5)

        btn_sjf = tk.Button(self.root, text="SJF", command=self.ejecutar_sjf, height=2, width=20,bg="lightblue", fg="darkblue")
        btn_sjf.grid(row=3, column=1, padx=10, pady=5)

        # Alineación de botones de abajo con los de arriba
        btn_agregar_proceso = tk.Button(self.root, text="Agregar Proceso", command=self.agregar_proceso, height=2, width=20, bg="lightgreen", fg="darkblue")
        btn_agregar_proceso.grid(row=4, column=0, padx=10, pady=5)  # Ajustar la columna según la alineación deseada

        btn_limpiar_consola = tk.Button(self.root, text="Limpiar Consola", command=self.limpiar_consola, height=2, width=20, bg="lightcoral", fg="darkred")
        btn_limpiar_consola.grid(row=4, column=1, padx=10, pady=5)  # Ajustar la columna según la alineación deseada


    def mostrar_consola(self, mensaje):
        self.consola.insert(tk.END, mensaje + "\n")
        self.consola.see(tk.END)

    def ejecutar_fifo(self):
        archivo = "procesos.txt"
        self.mostrar_consola("Ejecutando FIFO:")
        fifo.simulacion_FIFO(archivo)

    def ejecutar_prioridades(self):
        self.mostrar_consola("Ejecutando Prioridades:")
        self.ejecucion_procesos = True
        threading.Thread(target=self._ejecutar_prioridades).start()

    def _ejecutar_prioridades(self):
        prioridades.administrar_procesos_prioridades()
        self.ejecucion_procesos = False

    def ejecutar_rr(self):
        nombre_archivo = "procesos.txt"
        procesos = rr.cargar_procesos(nombre_archivo)
        self.mostrar_consola("Ejecutando Round Robin:")
        rr.round_robin(procesos)

    def ejecutar_sjf(self):
        procesos = sjf.leer_procesos()
        self.mostrar_consola("Ejecutando SJF:")
        sjf.ejecutar_sjf(procesos)

    def agregar_proceso(self):
        # Ventana de diálogo para ingresar los detalles del proceso
        dialogo = tk.Toplevel(self.root)
        dialogo.title("Agregar Proceso")
        dialogo.geometry("300x180")

        # Función para manejar el botón "Agregar"
        def agregar():
            nombre = nombre_entry.get()
            tiempo = tiempo_entry.get()
            prioridad = prioridad_entry.get()

            # Validación de entrada y escritura en el archivo si los valores son válidos
            if nombre and tiempo.isdigit() and prioridad.isdigit():
                with open("procesos.txt", "a") as archivo:
                    archivo.write(f"{nombre}, {tiempo}, {prioridad}\n")
                messagebox.showinfo("Proceso Agregado", "El proceso se ha agregado correctamente.")
                dialogo.destroy()
            else:
                messagebox.showwarning("Error", "Ingrese valores válidos para el proceso.")

        # Etiquetas y campos de entrada para nombre, tiempo y prioridad
        tk.Label(dialogo, text="(String) Nombre del proceso:").pack()
        nombre_entry = tk.Entry(dialogo)
        nombre_entry.pack()

        tk.Label(dialogo, text="(int) Tiempo de ejecución:").pack()
        tiempo_entry = tk.Entry(dialogo)
        tiempo_entry.pack()

        tk.Label(dialogo, text="(int) Prioridad:").pack()
        prioridad_entry = tk.Entry(dialogo)
        prioridad_entry.pack()

        # Botón para agregar el proceso
        btn_agregar = tk.Button(dialogo, text="Agregar", command=agregar, bg="lightgreen", fg="darkblue")
        btn_agregar.pack(padx=0, pady=15) 

    def salir_programa(self):
        if self.ejecucion_procesos:
            self.mostrar_consola("Deteniendo procesos...")
            
            
            self.ejecucion_procesos = False

        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
