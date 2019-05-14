# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime


from Practico_03A.ejercicio_02 import agregar_persona
from Practico_03A.ejercicio_01 import reset_tabla, engine, Persona
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def buscar_persona(id_persona):
    persona=session.query(Persona).filter(Persona.idPersona==id_persona).first()
    if (persona is None):
        return False
    else:
        datos=(persona.idPersona,persona.nombre,persona.fechaNacimiento,persona.dni,persona.altura)
        return datos


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
