import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from eventos1 import Calendario

class Bienvenida:
    def __init__(self, root):
        #setting title
        root.title("Calendario de eventos tp final upteco")
        #setting window size
        width=352
        height=182
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#333333"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "Bienvenidos al calendario de eventos"
        GLabel_764.place(x=90,y=20,width=205,height=74)

        GButton_955=tk.Button(root)
        GButton_955["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_955["font"] = ft
        GButton_955["fg"] = "#000000"
        GButton_955["justify"] = "center"
        GButton_955["text"] = "Entrar"
        GButton_955.place(x=80,y=120,width=70,height=25)
        GButton_955["command"] = self.boton_entrar

        GButton_435=tk.Button(root)
        GButton_435["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_435["font"] = ft
        GButton_435["fg"] = "#000000"
        GButton_435["justify"] = "center"
        GButton_435["text"] = "Salir"
        GButton_435.place(x=200,y=120,width=70,height=25)
        GButton_435["command"] = self.boton_salir

    def boton_entrar(self):
        Calendario(root)
        

    def boton_salir(self):
        root.destroy()
       
if __name__ == "__main__":
    root = tk.Tk()
    app = Bienvenida(root)
    root.mainloop()
    root.iconbitmap(default="calendario.ico")


