# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from Practico_03A.ejercicio_04 import buscar_persona
from Practico_03A.ejercicio_02 import agregar_persona
from Practico_03A.ejercicio_01 import reset_tabla, engine, Persona
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    encontrado=buscar_persona(id_persona)
    if encontrado is False:
        return False
    else:
        stmt = update(Persona)\
        .where(Persona.idPersona == id_persona)\
        .values(nombre=nombre,fechaNacimiento=nacimiento,dni=dni,altura=altura)
        session.execute(stmt)
        session.commit()


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16).strftime("%Y-%m-%d %H:%M:%S"), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
