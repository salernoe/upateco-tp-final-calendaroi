from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json
import tkinter.font as tkFont
from eventos3 import Evento

class NuevoEvento(tk.Toplevel):
   
   
    def __init__(self,marco, master=None ):
        super().__init__(master)        
        self.master = master
        self.marco = marco
        self.title("undefined")
        #setting window size
        width=436
        height=319
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.ingresar_nombre = tk.StringVar()
        self.ingresar_fecha = tk.StringVar()
        self.ingresar_hora = tk.StringVar()
        self.ingresar_descripcion = tk.StringVar()
        self.ingresar_importancia = tk.StringVar()

        GMessage_488=tk.Message(self)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_488["font"] = ft
        GMessage_488["fg"] = "#333333"
        GMessage_488["justify"] = "center"
        GMessage_488["text"] = "Ingreso de datos"
        GMessage_488.place(x=140,y=0,width=129,height=38)

        GLabel_710=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_710["font"] = ft
        GLabel_710["fg"] = "#333333"
        GLabel_710["justify"] = "center"
        GLabel_710["text"] = "Nombre"
        GLabel_710.place(x=10,y=40,width=70,height=25)

        ingresar_nombre=tk.Entry(self)
        ingresar_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ingresar_nombre["font"] = ft
        ingresar_nombre["fg"] = "#333333"
        ingresar_nombre["justify"] = "center"
        ingresar_nombre["text"] = "Entry"
        ingresar_nombre.place(x=80,y=40,width=259,height=30)

        GLabel_783=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_783["font"] = ft
        GLabel_783["fg"] = "#333333"
        GLabel_783["justify"] = "center"
        GLabel_783["text"] = "Fecha"
        GLabel_783.place(x=10,y=80,width=70,height=25)

        ingresar_fecha=tk.Entry(self)
        ingresar_fecha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ingresar_fecha["font"] = ft
        ingresar_fecha["fg"] = "#333333"
        ingresar_fecha["justify"] = "center"
        ingresar_fecha["text"] = "Entry"
        ingresar_fecha.place(x=80,y=80,width=259,height=30)

        GLabel_520=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_520["font"] = ft
        GLabel_520["fg"] = "#333333"
        GLabel_520["justify"] = "center"
        GLabel_520["text"] = "Hora"
        GLabel_520.place(x=10,y=120,width=70,height=25)

        ingresar_hora=tk.Entry(self)
        ingresar_hora["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ingresar_hora["font"] = ft
        ingresar_hora["fg"] = "#333333"
        ingresar_hora["justify"] = "center"
        ingresar_hora["text"] = "Entry"
        ingresar_hora.place(x=80,y=120,width=259,height=30)

        GLabel_45=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#333333"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "Descripcion"
        GLabel_45.place(x=0,y=160,width=70,height=25)

        ingresar_descripcion=tk.Entry(self)
        ingresar_descripcion["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ingresar_descripcion["font"] = ft
        ingresar_descripcion["fg"] = "#333333"
        ingresar_descripcion["justify"] = "center"
        ingresar_descripcion["text"] = "Entry"
        ingresar_descripcion.place(x=80,y=160,width=259,height=30)

        GLabel_545=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_545["font"] = ft
        GLabel_545["fg"] = "#333333"
        GLabel_545["justify"] = "center"
        GLabel_545["text"] = "Importancia"
        GLabel_545.place(x=0,y=200,width=70,height=25)

        ingresar_importancia=tk.Entry(self)
        ingresar_importancia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ingresar_importancia["font"] = ft
        ingresar_importancia["fg"] = "#333333"
        ingresar_importancia["justify"] = "center"
        ingresar_importancia["text"] = "Entry"
        ingresar_importancia.place(x=80,y=200,width=259,height=30)

        GButton_773=tk.Button(self)
        GButton_773["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_773["font"] = ft
        GButton_773["fg"] = "#000000"
        GButton_773["justify"] = "center"
        GButton_773["text"] = "Guardar"
        GButton_773.place(x=230,y=260,width=80,height=30)
        GButton_773["command"] = self.guardar_evento

        GButton_191=tk.Button(self)
        GButton_191["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_191["font"] = ft
        GButton_191["fg"] = "#000000"
        GButton_191["justify"] = "center"
        GButton_191["text"] = "Cancelar"
        GButton_191.place(x=320,y=260,width=80,height=30)
        GButton_191["command"] = self.cancelar_evento

    def actualizar_lista(self, evento):
        # add data to the treeview
        tk.insert('', tk.END, values=evento)

    def cancelar_evento(self):
       self.destroy()

    def guardar_evento(self,marco):
        eventos = Evento()
        eventos.set_ingresar_nombre(self.ingresar_nombre.get())
        eventos.set_ingresar_fecha(self.ingresar_fecha.get())
        eventos.set_ingresar_hora(self.ingresar_hora.get())
        eventos.set_ingresar_descripcion(self.ingresar_descripcion.get())
        eventos.set_ingresar_importancia(self.ingresar_importancia.get())
        eventos.guardar()

        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 0, "evento": []}         
        

        self.marco = marco
        evento = []
        evento.append(eventos["cantidad"])
        evento.append(self.ingresar_nombre.get())
        evento.append(self.ingresar_fecha.get())
        evento.append(self.ingresar_hora.get())
        evento.append(self.ingresar_descripcion.get())
        evento.append(self.ingresar_importancia.get())
        self.marco.actualizar_lista(eventos)

        self.parent.destroy()