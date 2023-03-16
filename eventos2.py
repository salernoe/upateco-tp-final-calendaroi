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
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("undefined")
        #setting window size
        width=436
        height=319
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

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

        GLineEdit_344=tk.Entry(self)
        GLineEdit_344["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_344["font"] = ft
        GLineEdit_344["fg"] = "#333333"
        GLineEdit_344["justify"] = "center"
        GLineEdit_344["text"] = "Entry"
        GLineEdit_344.place(x=80,y=40,width=259,height=30)

        GLabel_783=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_783["font"] = ft
        GLabel_783["fg"] = "#333333"
        GLabel_783["justify"] = "center"
        GLabel_783["text"] = "Fecha"
        GLabel_783.place(x=10,y=80,width=70,height=25)

        GLineEdit_159=tk.Entry(self)
        GLineEdit_159["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_159["font"] = ft
        GLineEdit_159["fg"] = "#333333"
        GLineEdit_159["justify"] = "center"
        GLineEdit_159["text"] = "Entry"
        GLineEdit_159.place(x=80,y=80,width=259,height=30)

        GLabel_520=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_520["font"] = ft
        GLabel_520["fg"] = "#333333"
        GLabel_520["justify"] = "center"
        GLabel_520["text"] = "Hora"
        GLabel_520.place(x=10,y=120,width=70,height=25)

        GLineEdit_86=tk.Entry(self)
        GLineEdit_86["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_86["font"] = ft
        GLineEdit_86["fg"] = "#333333"
        GLineEdit_86["justify"] = "center"
        GLineEdit_86["text"] = "Entry"
        GLineEdit_86.place(x=80,y=120,width=259,height=30)

        GLabel_45=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#333333"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "Descripcion"
        GLabel_45.place(x=0,y=160,width=70,height=25)

        GLineEdit_0=tk.Entry(self)
        GLineEdit_0["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_0["font"] = ft
        GLineEdit_0["fg"] = "#333333"
        GLineEdit_0["justify"] = "center"
        GLineEdit_0["text"] = "Entry"
        GLineEdit_0.place(x=80,y=160,width=259,height=30)

        GLabel_545=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_545["font"] = ft
        GLabel_545["fg"] = "#333333"
        GLabel_545["justify"] = "center"
        GLabel_545["text"] = "Importancia"
        GLabel_545.place(x=0,y=200,width=70,height=25)

        GLineEdit_477=tk.Entry(self)
        GLineEdit_477["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_477["font"] = ft
        GLineEdit_477["fg"] = "#333333"
        GLineEdit_477["justify"] = "center"
        GLineEdit_477["text"] = "Entry"
        GLineEdit_477.place(x=80,y=200,width=259,height=30)

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

    #def guardar_evento(self):
       # toplevel = tk.Toplevel(self.parent)
       # Alta(toplevel, self).grid()

    def cancelar_carga(self):
       self.destroy()

class Alta(ttk.Frame):
    def __init__(self, parent, marco):
        super().__init__(parent, padding=(20))
        self.parent = parent
        self.marco = marco
        parent.title("Nueva Evento")
        parent.geometry("500x300+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)

        self.nombre = tk.StringVar()
        self.fecha = tk.StringVar()
        self.hora = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.importancia = tk.StringVar() 
    
    def cancelar_carga(self):
       self.destroy()

    def guardar_evento(self):
        eventos = Evento()
        eventos.set_nombre(self.evento.get())
        eventos.set_fecha(self.fecha.get())
        eventos.set_hora(self.hora.get())
        eventos.set_descripcion(self.descripcion.get())
        eventos.set_importancia(self.importancia.get())
        eventos.guardar()

        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 0, "evento": []}         
        
        evento = []
        evento.append(eventos["cantidad"])
        evento.append(self.nombre.get())
        evento.append(self.hora.get())
        evento.append(self.fecha.get())
        evento.append(self.descripcion.get())
        evento.append(self.importancia.get())
        self.marco.actualizar_lista(eventos)

        self.parent.destroy()