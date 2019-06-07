## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

import tkinter as Tkinter
from tkinter import *

class Ciudades(Tkinter.Frame):


    def __init__(self, parent): #Constructor
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.var1 = DoubleVar()
        self.var2 = DoubleVar()
        self.resultado=StringVar()
        self.ancho_entry=25
        self.ancho_boton=5

        self.parent.title("Calculadora Simple")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="light blue")


        #Se definen los labels y cuadros de ingreso de datos
        self.var1_label = Tkinter.Label(self.parent, text = "Número 1:")
        self.var1_entry = Tkinter.Entry(self.parent,width=self.ancho_entry,textvariable=self.var1)
        self.var1_label.grid(row = 0, column = 0, sticky = Tkinter.W)
        self.var1_entry.grid(row = 0, column = 1)
        self.var2_label = Tkinter.Label(self.parent, text = "Número 2:")
        self.var2_entry = Tkinter.Entry(self.parent,width=self.ancho_entry,textvariable=self.var2)
        self.var2_label.grid(row = 1, column = 0, sticky = Tkinter.W)
        self.var2_entry.grid(row = 1, column = 1)

        self.resultado_label = Tkinter.Label(self.parent, text = "Resultado:")
        self.resultado_entry = Tkinter.Entry(self.parent,width=self.ancho_entry, textvariable=self.resultado)
        self.resultado_label.grid(row = 3, column = 0, sticky = Tkinter.W)
        self.resultado_entry.grid(row = 3, column = 1)
        self.sumar_boton = Tkinter.Button(self.parent, text = "+",width=self.ancho_boton, command = lambda:self.suma(self.var1,self.var2))
        self.sumar_boton.grid(row = 4, column = 0)
        self.restar_boton = Tkinter.Button(self.parent, text="-",width=self.ancho_boton, command = lambda:self.resta(self.var1,self.var2))
        self.restar_boton.grid(row=4,column=1,sticky = Tkinter.W)
        self.mulp_boton = Tkinter.Button(self.parent, text="*",width=self.ancho_boton, command = lambda:self.multiplicacion(self.var1,self.var2))
        self.mulp_boton.grid(row=4,column=1, sticky = Tkinter.S)
        self.div_boton = Tkinter.Button(self.parent, text="/",width=self.ancho_boton,command = lambda:self.division(self.var1,self.var2))
        self.div_boton.grid(row=4,column=1, sticky = Tkinter.E)
        self.salir_boton = Tkinter.Button(self.parent, text = "Salir",width=self.ancho_boton, command = self.parent.quit)
        self.salir_boton.grid(row = 4, column = 5)

    def suma(self,var1,var2):
        suma=var1.get() + var2.get()
        self.resultado.set(suma)

    def resta(self,var1,var2):
        resta=var1.get() - var2.get()
        self.resultado.set(resta)

    def multiplicacion(self,var1,var2):
        mult=var1.get() * var2.get()
        self.resultado.set(mult)

    def division(self,var1,var2):
        try:
            div=var1.get() / var2.get()
            self.resultado.set(div)
        except:
            self.resultado.set("ERROR!")


def main():
    root=Tkinter.Tk()
    Ciudades(root)
    root.mainloop()

if __name__=="__main__":
    main()
