# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import time
class Persona:

    def __init__(self,nombre,edad,sexo,peso,altura,dni):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.altura=altura
        self.dni=dni

    def print_data(self):
        print('Nombre:',self.nombre)
        print('Edad:',self.edad)
        print('Sexo:',self.sexo)
        print('Peso:',self.peso,'Kg')
        print('Altura:',self.altura,'m')
        print('DNI:',self.dni)

class Estudiante(Persona):

    def __init__(self,nombre,edad,sexo,peso,altura,dni,carrera,anioIngreso,cantidadMaterias,cantidadMateriasAprobadas):
        Persona.__init__(self,nombre,edad,sexo,peso,altura,dni)
        self.carrera=carrera
        self.anioIngreso=anioIngreso
        self.cantidadMaterias=cantidadMaterias
        self.cantidadMateriasAprobadas=cantidadMateriasAprobadas

    def avance(self):
        porcentaje=('{0:.2f}'.format((self.cantidadMateriasAprobadas/self.cantidadMaterias)*100))
        return porcentaje

    def edad_ingreso(self):
        edadIng=(self.edad-(int(time.strftime('%Y'))-self.anioIngreso))
        return edadIng

estudiante=Estudiante('Agustin Yurescia',22,'H',69.60,1.75,'39.291.780','ISI',2015,41,27)
assert estudiante.edad_ingreso() == 18
assert estudiante.avance() == '65.85'


