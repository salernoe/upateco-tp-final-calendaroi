from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json

class Evento:
    def __init__(self):
        self.nombre = ""
        self.fecha = ""
        self.hora = ""
        self.descripcion = ""
        self.importancia = ""
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self,hora):
        self.hora = hora

    def descripcion(self, descripcion):
        self.descripcion = descripcion

    def importancia(self, importancia):
        self.importancia = importancia


    def get_elemento_tupla(self):
        evento = ()
        evento.append(self.nombre)
        evento.append(self.fecha)
        evento.append(self.hora)
        evento.append(self.descripcion)
        evento.append(self.importancia)
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

        #recetas["cantidad"] = int(recetas["cantidad"])

        #print(recetas)

        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)
    
    def guardar(self):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 0, "recetas": []}         
        
        evento = {}
        evento["id"] = int(eventos["cantidad"])+1
        evento["nombre"] = self.nombre
        evento["fecha"] = self.fecha
        evento["hora"] = self.hora
        evento["descripcion"] = self.descripcion
        evento["importancia"] = self.importancia
        evento["eventos"].append(evento)
        evento["cantidad"] = int(eventos["cantidad"])+1
        
        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)

    def guardarV1(self):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = []          
        evento = {}
        evento["nombre"] = self.nombre
        evento["fecha"] = self.fecha
        evento["hora"] = self.hora
        evento["descripcion"] = self.descripcion
        evento["importancia"] = self.importancia
        eventos.append(evento)
        
        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)