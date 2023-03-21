from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json

class Evento:
    def __init__(self):
        self.id = ""
        self.ingresar_nombre = ""
        self.ingresar_fech = ""
        self.ingresar_hora = ""
        self.ingresar_descripcion = ""
        self.ingresar_importancia= ""

    def set_id(self, id):
        self.id = id
    
    def set_ingresar_nombre(self, ingresar_nombre):
        self.ingresar_nombre = ingresar_nombre
    
    def set_ingresar_fecha(self, ingresar_fecha):
        self.ingresar_fecha = ingresar_fecha

    def set_ingresar_hora(self,ingresar_hora):
        self.ingresar_hora = ingresar_hora

    def ingresar_descripcion(self, ingresar_descripcion):
        self.ingresar_descripcion = ingresar_descripcion

    def ingresar_importancia(self, ingresar_importancia):
        self.ingresar_importancia = ingresar_importancia


    def get_elemento_tupla(self):
        evento = ()
        evento.append(self.ingresar_nombre)
        evento.append(self.ingresar_fecha)
        evento.append(self.ingresar_hora)
        evento.append(self.ingresar_descripcion)
        evento.append(self.ingresar_importancia)
        return evento
    
    @staticmethod
    def eliminar(id_evento):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                pass
        #print(eventos)
        aux = []
        for elem in eventos["eventos"]:
            if elem['id'] != id_evento:
                aux.append(elem)

        eventos["eventos"] = aux

       
        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)
    
    def guardar(self):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 0, "eventos": []}         
        
        evento = {}
        evento["id"] = int(eventos["cantidad"])+1
        evento["ingresar_nombre"] = self.ingresar_nombre
        evento["ingresar_fecha"] = self.ingresar_fecha
        evento["ingresar_hora"] = self.ingresar_hora
        evento["ingresar_descripcion"] = self.ingresar_descripcion
        evento["ingresar_importancia"] = self.ingresar_importancia
        evento["eventos"].append(evento)
        evento["cantidad"] = int(eventos["cantidad"])+1
        
        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)
    
    def editar(self, id_evento):
        print('editar')
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                pass
        aux = []
        for elem in eventos["eventos"]:
            if elem['id'] != id_evento:
                aux.append(elem)
            else:
                evento = {}
                evento["id"] = id_evento
                evento["ingresar_nombre"] = self.ingresar_nombre
                evento["ingresar_fech"] = self.ingresar_fech
                evento["ingresar_hora"] = self.ingresar_hora
                evento["ingresar_descripcion"] = self.ingresar_descripcion
                evento["ingresar_importancia"] = self.ingresar_importancia
                aux.append(evento)
                print(evento)
        eventos["eventos"] = aux

        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)

    