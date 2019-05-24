# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from Practico_03A.ejercicio_01 import reset_tabla, engine, Persona
from sqlalchemy.orm import sessionmaker


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_persona(nombre, nacimiento, dni, altura):
    oper = Persona()
    oper.nombre=nombre
    oper.fechaNacimiento=nacimiento
    oper.dni=dni
    oper.altura=altura
    session.add(oper)
    session.commit()
    return oper.idPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25).strftime("%Y-%m-%d %H:%M:%S"), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()

