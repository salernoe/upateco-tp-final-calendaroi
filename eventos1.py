import tkinter as tk
from tkinter import ttk
import json

class Calendario(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent    # guardamos una referencia de la ventana ppal
        parent.title("Calendario de eventos")
        parent.geometry("1050x600+100+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)

        columns = ('id_evento', 'nombre', 'fecha', 'hora', 'descrpcion','importacia')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_evento', text='ID')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='hora')
        self.tree.heading('descrpcion', text='Descrpcion')
        self.tree.heading('importacia', text='importacia')

        self.get_elemento_lista()
        
        self.tree.grid(row=0, column=0, padx = 5, pady = 5)

        ttk.Button(self, text="Nuevo", command=self.abrir_ventana).grid()
        ttk.Button(self, text="Eliminar", command=self.eliminar_evento).grid()
        # ejecutar callback cuando se seleccione (o des-seleccione) una fila
        self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado)

    def item_seleccionado(self, event):
        seleccion = self.tree.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = self.tree.item(item_id) # obtenemos el item y sus datos
                fila = item['values'][0]
                print(fila)
    
    def abrir_ventana(self):
        # creamos la ventana Alta
        # como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Alta) a la ventana (toplevel)
        Alta(toplevel, self).grid()

    def get_elemento_lista(self):
        # add data to the treeview
        # leemos los datos
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = []
        lista_eventos = []

        #generamos los datos
        for evento in eventos[" eventos"]:
            lista_eventos.append(( evento["id"], evento["nombre"],  evento["fecha"],  evento["hora"], evento["descripcion"], evento["importacia"]))
        # add data to the treeview
        for evento in lista_eventos:
            self.tree.insert('', tk.END, values=evento)

        self.eliminar_evento()

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = self.tree.item(item_id) # obtenemos el item y sus datos
                id_evento = item['values'][0] # capturo el id de mi registro
                Evento.eliminar(id_evento) # actualizo mi .json
                self.tree.delete(item_id) # actualizo treeview

    def actualizar_lista(self, receta):
        # add data to the treeview
        self.tree.insert('', tk.END, values=receta)

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

        self.nombre_receta = tk.StringVar()
        self.tiempo_preparacion = tk.StringVar()
        self.tiempo_coccion = tk.StringVar()
        self.fecha_creacion = tk.StringVar()

        ttk.Label(self, text="Nombre:").grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.nombre_receta).grid(row=1, column=2)
        ttk.Label(self, text="Tiempo preparación:").grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.tiempo_preparacion).grid(row=2, column=2)
        ttk.Label(self, text="Tiempo cocción:").grid(row=3, column=1)
        ttk.Entry(self, textvariable=self.tiempo_coccion).grid(row=3, column=2)
        ttk.Label(self, text="Fecha creación:").grid(row=4, column=1)
        ttk.Entry(self, textvariable=self.fecha_creacion).grid(row=4, column=2)
        
        ttk.Button(self, text="Guardar", command=self.guardar_receta).grid(row=5, column=1)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid(row=5, column=3)

    def guardar_receta(self):
        recetas = Evento()
        recetas.set_nombre(self.nombre_receta.get())
        recetas.set_tiempo_preparacion(self.tiempo_preparacion.get())
        recetas.set_tiempo_coccion(self.tiempo_coccion.get())
        recetas.set_fecha_creacion(self.fecha_creacion.get())
        recetas.guardar()

        with open("eventos.json", 'r') as archivo:
            try:
                recetas = json.load(archivo)
            except ValueError:
                recetas = {"cantidad": 0, "recetas": []}         
        
        receta = []
        receta.append(recetas["cantidad"])
        receta.append(self.nombre_receta.get())
        receta.append(self.tiempo_preparacion.get())
        receta.append(self.tiempo_coccion.get())
        receta.append(self.fecha_creacion.get())
        self.marco.actualizar_lista(receta)

        self.parent.destroy()

class Evento:
    def __init__(self):
        self.nombre = ""
        self.tiempo_preparacion = ""
        self.tiempo_coccion = ""
        self.fecha_creacion = ""
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_tiempo_preparacion(self, tiempo_preparacion):
        self.tiempo_preparacion = tiempo_preparacion

    def set_tiempo_coccion(self, tiempo_coccion):
        self.tiempo_coccion = tiempo_coccion

    def set_fecha_creacion(self, fecha_creacion):
        self.fecha_creacion = fecha_creacion

    def get_elemento_tupla(self):
        receta = ()
        receta.append(self.nombre)
        receta.append(self.tiempo_preparacion)
        receta.append(self.tiempo_coccion)
        receta.append(self.fecha_creacion)
        return receta
    
    @staticmethod
    def eliminar(id_receta):
        with open("eventos.json", 'r') as archivo:
            try:
                recetas = json.load(archivo)
            except ValueError:
                pass
        #print(recetas)
        aux = []
        for elem in recetas["recetas"]:
            if elem['id'] != id_receta:
                aux.append(elem)

        recetas["recetas"] = aux

        #recetas["cantidad"] = int(recetas["cantidad"])

        #print(recetas)

        with open("eventos.json", 'w') as archivo:
            json.dump(recetas, archivo)
    
    def guardar(self):
        with open("eventos.json", 'r') as archivo:
            try:
                recetas = json.load(archivo)
            except ValueError:
                recetas = {"cantidad": 0, "recetas": []}         
        
        receta = {}
        receta["id"] = int(recetas["cantidad"])+1
        receta["nombre"] = self.nombre
        receta["tiempo_preparacion"] = self.tiempo_preparacion
        receta["tiempo_coccion"] = self.tiempo_coccion
        receta["fecha_creacion"] = self.fecha_creacion
        recetas["recetas"].append(receta)
        recetas["cantidad"] = int(recetas["cantidad"])+1
        
        with open("eventos.json", 'w') as archivo:
            json.dump(recetas, archivo)

    def guardarV1(self):
        with open("eventos.json", 'r') as archivo:
            try:
                recetas = json.load(archivo)
            except ValueError:
                recetas = []          
        receta = {}
        receta["nombre"] = self.nombre
        receta["tiempo_preparacion"] = self.tiempo_preparacion
        receta["tiempo_coccion"] = self.tiempo_coccion
        receta["fecha_creacion"] = self.fecha_creacion
        recetas.append(receta)
        
        with open("eventos.json", 'w') as archivo:
            json.dump(recetas, archivo)

