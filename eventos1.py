from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json
from eventos2 import NuevoEvento
from eventos3 import Evento
from eventos4 import Editar

class Calendario(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Calendario de eventos tp final upteco")        
        width=900
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = " Calendario de Eventos"
        GLabel_464.place(x= 300,y=10,width=200,height=40)

        tk = ttk.Treeview(self, columns=("Nombre", "Fecha", "Hora","Descripcion","Importacia"), name="tkDescuentos")
        tk.column("#0", width=78)
        tk.column("Nombre", width=150, anchor=CENTER)
        tk.column("Fecha", width=150, anchor=CENTER)
        tk.column("Hora", width=150, anchor=CENTER)
        tk.column("Descripcion", width=150, anchor=CENTER)
        tk.column("Importacia", width=150, anchor=CENTER)
        
        tk.heading("#0", text="ID", anchor=CENTER)
        tk.heading("Nombre", text="Nombre", anchor=CENTER)
        tk.heading("Fecha", text="Fecha", anchor=CENTER)
        tk.heading("Hora", text="Hora", anchor=CENTER)   
        tk.heading("Descripcion", text="Descripcion", anchor=CENTER)
        tk.heading("Importacia", text="Importacia", anchor=CENTER)

        tk.bind("<<TreeviewSelect>>", self.obtener_fila)
        tk.place(x=10,y=50,width=820,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "NUEVO"
        btn_agregar.place(x=360,y=360,width=100,height=30)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "EDITAR"
        btn_editar.place(x=470,y=360,width=100,height=30)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "ELIMINAR"
        btn_eliminar.place(x=580,y=360,width=100,height=30)
        btn_eliminar["command"] = self.eliminar
        
        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#000000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "SALIR"
        btn_salir.place(x=690,y=360,width=100,height=30)
        btn_salir["command"] = self.salir

    def item_seleccionado(self, event):
        seleccion = tk.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = tk.item(item_id) # obtenemos el item y sus datos
                fila = item['values'][0]

    def obtener_fila(self, event):
        tkDescuentos = self.nametowidget("tkDescuentos")
        current_item = tkDescuentos.focus()
        if current_item:
            data = tkDescuentos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        NuevoEvento(self.master)

    def get_elemento_lista(self):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 1, "eventos":[]}
        lista_eventos = []

        #generamos los datos
        for evento in eventos["eventos"]:
           lista_eventos.append ((evento["id"],evento["ingresar_nombre"], evento["ingresar_fecha"], evento["ingresar_hora"], evento["ingresar_descripcion"],evento["ingresar_importancia"]))
        # add data to the treeview
        for evento in lista_eventos:
            tk.insert('', 'end', text=evento[0], values=evento)

        
    def editar(self): 
        seleccion = tk.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = tk.item(item_id) # obtenemos el item y sus datos
                id_evento = item['values'][0] # capturo el id de mi registro
                #Receta.eliminar(id_receta) # actualizo mi .json
                #self.tree.delete(item_id) # actualizo treeview

                # creamos la ventana Alta
                # como padre indicamos la ventana principal
                toplevel = tk.Toplevel(self)
                # agregamos el frame (Alta) a la ventana (toplevel)
                self.agregar = Editar(toplevel, self)
                self.agregar.grid() 
                
                self.agregar.set_id(item['values'][0])
                self.agregar.set_ingresar_nombre(item['values'][1])
                self.agregar.set_ingresar_fecha(item['values'][2])
                self.agregar.set_ingresar_hora(item['values'][3])
                self.agregar.set_ingresar_descripcion(item['values'][4])
                self.agregar.set_ingresar_importancia(item['values'][5])


    """def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este descuento?")   
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = []
        lista_eventos = []

        #generamos los datos
        for evento in eventos["eventos"]:
            lista_eventos.append(( evento["id"], evento["nombre"],  evento["fecha"],  evento["hora"], evento["descripcion"], evento["importacia"]))
        
        for evento in lista_eventos:
            tk.insert('', tk.END, values=evento)"""

        

    def eliminar(self):
        seleccion = tk.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = tk.item(item_id) # obtenemos el item y sus datos
                id_evento = item['values'][0] # capturo el id de mi registro
                Evento.eliminar(id_evento) # actualizo mi .json
                tk.delete(item_id) # actualizo treeview

    def actualizar_lista(self, evento):
        # add data to the treeview
        tk.insert('', tk.END, values=evento)
        
            
    def salir(self):
        self.destroy()
    
    def refrescar(self):        
        """tkDescuentos = self.nametowidget("tkDescuentos")
        for record in tkDescuentos.get_children():
            tkDescuentos.delete(record)
        descuentos = NuevoEvento.listar()
        for descuento in descuentos:
            tkDescuentos.insert("", END, text=descuento[0], values=(descuento[1], descuento[2], descuento[3])) """
        pass