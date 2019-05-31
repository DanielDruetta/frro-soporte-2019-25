## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .
 
from tkinter import *
from tkinter import ttk
from math import *

ventana = Tk()
ventana.geometry('395x240')
ventana.resizable(0, 0)
ventana.title('Calculadora')


def click(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)#ESTA PARTE SIRVE PARA VISUALIZAR LA OPERACION EN LA PANTALLA

def limpiar():
    global operador
    operador=("")
    input_text.set("0")

def operacion():
    global operador
    try:
        opera=str(eval(operador))#SIRVE PARA REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
    except:
        limpiar()
        opera=("ERROR")
    input_text.set(opera)#MUESTRA EL RESULTADO

ancho_boton=10
alto_boton=3
input_text=StringVar()
operador=""
limpiar()
Boton1=Button(ventana, text='1' ,width=ancho_boton,height=alto_boton, command=lambda:click(1)).grid(row=3, column=1)
Boton2=Button(ventana, text='2' ,width=ancho_boton,height=alto_boton, command=lambda:click(2)).grid(row=3, column=2)
Boton3=Button(ventana, text='3' ,width=ancho_boton,height=alto_boton, command=lambda:click(3)).grid(row=3, column=3)
Boton4=Button(ventana, text='4' ,width=ancho_boton,height=alto_boton, command=lambda:click(4)).grid(row=4, column=1)
Boton5=Button(ventana, text='5' ,width=ancho_boton,height=alto_boton, command=lambda:click(5)).grid(row=4, column=2)
Boton6=Button(ventana, text='6' ,width=ancho_boton,height=alto_boton, command=lambda:click(6)).grid(row=4, column=3)
Boton7=Button(ventana, text='7' ,width=ancho_boton,height=alto_boton, command=lambda:click(7)).grid(row=5, column=1)
Boton8=Button(ventana, text='8' ,width=ancho_boton,height=alto_boton, command=lambda:click(8)).grid(row=5, column=2)
Boton9=Button(ventana, text='9' ,width=ancho_boton,height=alto_boton, command=lambda:click(9)).grid(row=5, column=3)
Boton0=Button(ventana, text='0' ,width=ancho_boton,height=alto_boton, command=lambda:click(0)).grid(row=6, column=2)
BotonMas=Button(ventana, text='+' ,width=ancho_boton,height=alto_boton, command=lambda:click("+")).grid(row=3, column=4)
BotonMen=Button(ventana, text='-' ,width=ancho_boton,height=alto_boton, command=lambda:click("-")).grid(row=4, column=4)
BotonMult=Button(ventana, text='*' ,width=ancho_boton,height=alto_boton, command=lambda:click("*")).grid(row=3, column=5)
BotonDiv=Button(ventana, text='/' ,width=ancho_boton,height=alto_boton, command=lambda:click("/")).grid(row=4, column=5)
BotonBorrar=Button(ventana, text='C',width=ancho_boton,height=alto_boton, command=limpiar).grid(row=5, column=5)
BotonIgual=Button(ventana, text='=',width=ancho_boton,height=alto_boton, command=operacion).grid(row=5, column=4)
Salida=Entry(ventana,width=ancho_boton,textvariable=input_text,justify="right").grid(row=1, column=3)

ventana.mainloop()
