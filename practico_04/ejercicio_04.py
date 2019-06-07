## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

import tkinter as Tkinter
from tkinter import ttk
from tkinter import *

class Ciudades(Tkinter.Frame):

    def __init__(self, parent): #Constructor
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.nroBaja = StringVar()
        self.nroEditar = StringVar()
        self.nuevoCP = StringVar()
        self.nuevoNombre = StringVar()

        self.parent.title("Ciudades y Capitales")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="light blue")

        #Se definen los labels y cuadros de ingreso de datos

        #Label y entry para ingreso del nombre de una ciudad
        self.ciudad_label = Tkinter.Label(self.parent, text = "Ciudad:",background="light blue")
        self.ciudad_entry = Tkinter.Entry(self.parent)
        self.ciudad_label.grid(row = 0, column = 0, sticky = Tkinter.W)
        self.ciudad_entry.grid(row = 0, column = 0)

        #Label y entry para para ingreso de código postal
        self.cp_label = Tkinter.Label(self.parent, text = "Codigo Postal:",background="light blue")
        self.cp_entry = Tkinter.Entry(self.parent)
        self.cp_label.grid(row = 1, column = 0, sticky = Tkinter.W)
        self.cp_entry.grid(row = 1, column = 0)

        #Label y entry para eliminar una ciudad
        self.nroBajaCiudad_label = Tkinter.Label(self.parent, text = "Nro Ciudad a Dar de Baja:",background="light blue")
        self.nroBajaCiudad_entry = Tkinter.Entry(self.parent, textvariable=self.nroBaja)
        self.nroBajaCiudad_label.grid(row = 3, column = 0, sticky = Tkinter.W)
        self.nroBajaCiudad_entry.grid(row = 3, column = 0)

        #Botón para carga de datos
        self.insertar_boton = Tkinter.Button(self.parent, text = "Insertar", command = self.insertar_data)
        self.insertar_boton.grid(row = 2, column = 0)

        #Botón para eliminar
        self.baja_boton = Tkinter.Button(self.parent, text="Dar de baja", command = lambda:self.baja_data(self.nroBaja.get()))
        self.baja_boton.grid(row=4,column=0)

        #Label y entry de nro de ciudad a editar
        self.nroCiudadEditar_label = Tkinter.Label(self.parent, text = "Nro Ciudad a Editar CP:",background="light blue")
        self.nroCiudadEditar_entry = Tkinter.Entry(self.parent, textvariable=self.nroEditar)
        self.nroCiudadEditar_label.grid(row = 5, column = 0, sticky = Tkinter.W)
        self.nroCiudadEditar_entry.grid(row = 5, column = 0)

        #Label y entry del nombre de la ciudad a editar
        self.nuevaCiudadEditar_label = Tkinter.Label(self.parent, text = "Nuevo Nombre Ciudad:",background="light blue")
        self.nuevaCiudadEditar_entry = Tkinter.Entry(self.parent, textvariable=self.nuevoNombre)
        self.nuevaCiudadEditar_label.grid(row = 6, column = 0, sticky = Tkinter.W)
        self.nuevaCiudadEditar_entry.grid(row = 6, column = 0)

        #Label y entry del código postal a editar
        self.cpCiudadEditar_label = Tkinter.Label(self.parent, text = "Nuevo CP:",background="light blue")
        self.cpCiudadEditar_entry = Tkinter.Entry(self.parent, textvariable=self.nuevoCP)
        self.cpCiudadEditar_label.grid(row = 7, column = 0, sticky = Tkinter.W)
        self.cpCiudadEditar_entry.grid(row = 7, column = 0)

        #Botón de salir
        self.editar_boton = Tkinter.Button(self.parent, text = "Editar",width=15, command = lambda:self.editar_data(self.nroEditar.get(),self.nuevoNombre.get(),self.nuevoCP.get()))
        self.editar_boton.grid(row = 8, column = 0)

        #Botón de editar
        self.salir_boton = Tkinter.Button(self.parent, text = "Salir", command = self.parent.quit)
        self.salir_boton.grid(row = 9, column = 1)

        #Se crea el treeview
        self.tree = ttk.Treeview( self.parent, columns=('Ciudad', 'Codigo Postal'))
        self.tree.heading('#0', text='Nro de Ciudad')
        self.tree.heading('#1', text='Ciudad')
        self.tree.heading('#2', text='Codigo Postal')
        self.tree.column('#1', stretch=Tkinter.YES)
        self.tree.column('#2', stretch=Tkinter.YES)
        self.tree.column('#0', stretch=Tkinter.YES)
        self.tree.grid(row=10, columnspan=10, sticky='nsew')
        self.treeview = self.tree
        self.i = 0   #Inicializo contador para guardar el nro de ciudad ingresada

    #Método para borrar datos
    def baja_data(self,nro_ciudad):
        self.treeview.delete(nro_ciudad) #Borra el item con iid=nro_ciudad
        self.nroBaja.set("")

    #Método para la carga de los datos
    def insertar_data(self):
        self.treeview.insert('', 'end', text=str(self.i), values=(self.ciudad_entry.get(), self.cp_entry.get()),iid=self.i)
        self.i = self.i + 1 #Incremento el contador de nro de ciudad

    #Método que busca y edita los datos de una fila
    def editar_data(self,nro,nombre,cp):
        self.treeview.item(nro, values=(nombre,cp))
        self.nroEditar.set("")
        self.nuevoNombre.set("")
        self.nuevoCP.set("")

def main():
    root=Tkinter.Tk()
    Ciudades(root)
    root.mainloop()

if __name__=="__main__":
    main()
