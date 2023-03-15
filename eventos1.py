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

    def actualizar_lista(self, evento):
        # add data to the treeview
        self.tree.insert('', tk.END, values=evento)

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

        ttk.Label(self, text="Nombre:").grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.nombre).grid(row=1, column=2)
        ttk.Label(self, text="Fecha:").grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.fecha).grid(row=2, column=2)
        ttk.Label(self, text="Hora:").grid(row=3, column=1)
        ttk.Entry(self, textvariable=self.hora).grid(row=3, column=2)
        ttk.Label(self, text="Descripcion:").grid(row=4, column=1)
        ttk.Entry(self, textvariable=self.descripcion).grid(row=4, column=2)
        ttk.Label(self, text="Importancia:").grid(row=5, column=1)
        ttk.Entry(self, textvariable=self.importancia).grid(row=5, column=2)


        ttk.Button(self, text="Guardar", command=self.guardar_evento).grid(row=5, column=1)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid(row=5, column=3)

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
                eventos = {"cantidad": 0, "recetas": []}         
        
        receta = []
        receta.append(eventos["cantidad"])
        receta.append(self.nombre.get())
        receta.append(self.hora.get())
        receta.append(self.fecha.get())
        receta.append(self.descripcionn.get())
        receta.append(self.importancia.get())
        self.marco.actualizar_lista(eventos)

        self.parent.destroy()

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

root = tk.Tk()
Calendario(root).grid()
root.mainloop()