from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json
from eventos2 import NuevoEvento
from eventos3 import Evento



class Editar(ttk.Frame):
   
    def __init__(self, parent, marco):
        super().__init__(parent, padding=(20))
        self.parent = parent
        self.marco = marco
        parent.title("Calendario de eventos")
        parent.geometry("500x300+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        
        self.id = None
        self.ingresar_nombre = tk.StringVar()
        self.ingresar_fecha = tk.StringVar()
        self.ingresar_hora = tk.StringVar()
        self.ingresar_descripcion = tk.StringVar()
        self.ingresar_importancia = tk.StringVar()
   
        ttk.Label(self, text="Nombre:").grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.ingresar_nombre).grid(row=1, column=2)
        ttk.Label(self, text="Fecha:").grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.ingresar_fecha).grid(row=2, column=2)
        ttk.Label(self, text="Hora:").grid(row=3, column=1)
        ttk.Entry(self, textvariable=self.ingresar_hora).grid(row=3, column=2)
        ttk.Label(self, text="Descripcion:").grid(row=4, column=1)
        ttk.Entry(self, textvariable=self.ingresar_descripcion).grid(row=4, column=2)
        ttk.Label(self, text=" Importancia:").grid(row=4, column=1)
        ttk.Entry(self, textvariable=self.ingresar_importancia).grid(row=5, column=2)


        ttk.Button(self, text="Guardar", command=self.editar_evento).grid(row=5, column=1)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid(row=5, column=3)

    def set_id(self, id):
        self.id = id

    def set_ingresar_nombre(self,nombre):
        self.ingresar_nombre.set(nombre)
    
    def set_ingresar_fecha(self, ingresar_fecha):
        self.ingresar_fecha.set(ingresar_fecha)

    def set_ingresar_hora(self, ingresar_hora):
        self.ingresar_hora.set(ingresar_hora)

    def set_ingresar_descripcion(self, ingresar_descripcion):
        self.ingresar_descripcion.set(ingresar_descripcion)
    
    def set_ingresar_importancia(self, ingresar_importancia):
        self.ingresar_importancia.set(ingresar_importancia)

    def editar_evento(self):
        eventos = Evento()
        eventos.set_id(self.id)
        eventos.set_ingresar_nombre(self.ingresar_nombre.get())
        eventos.set_ingresar_fecha(self.ingresar_fecha.get())
        eventos.set_ingresar_hora(self.ingresar_hora.get())
        eventos.set_ingresar_descripcion(self.ingresar_descripcion.get())
        eventos.set_ingresar_importancia(self.ingresar_importancia.get())
        eventos.editar(self.id)
        
        self.marco.clear_all()
        self.marco.get_elemento_lista()


        self.parent.destroy()
            
