# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    far=((grados*9/5)+32)
    return far
assert conversor(1) == 33.8

#Para pedir el ingreso del dato por teclado y devolver el valor en Farenheit:
#grados = float(input('Introduzca una temperatura en grados celsius: '))
#print('\nLa temperatura en Farenheit es: ',conversor(grados))
