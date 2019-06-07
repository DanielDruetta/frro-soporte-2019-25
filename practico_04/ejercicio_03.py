## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

import tkinter as Tkinter
from tkinter import ttk

class Ciudades(Tkinter.Frame):

    def __init__(self, parent):     #Constructor
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.parent.title("Ciudades y Capitales")

        #Se crea el treeview
        self.tree = ttk.Treeview( self.parent, columns=('Ciudad', 'Codigo Postal'))
        self.tree.heading('#0', text='Nro de Ciudad')
        self.tree.heading('#1', text='Ciudad')
        self.tree.heading('#2', text='Código Postal')
        self.tree.column('#1', stretch=Tkinter.YES)
        self.tree.column('#2', stretch=Tkinter.YES)
        self.tree.column('#0', stretch=Tkinter.YES)
        self.tree.grid(row=6, columnspan=6, sticky='nsew')
        self.treeview = self.tree

        #Carga de datos (5 ciudades)
        self.treeview.insert('', 'end', text='1', values=("Vedia","6030"))
        self.treeview.insert('', 'end', text='2', values=("Buenos Aires","7020"))
        self.treeview.insert('', 'end', text='3', values=("Rosario","2000"))
        self.treeview.insert('', 'end', text='4', values=("Santa Fe","2004"))
        self.treeview.insert('', 'end', text='5', values=("San Juan","4050"))

def main():
    root=Tkinter.Tk()
    Ciudades(root)
    root.mainloop()

if __name__=="__main__":
    main()
