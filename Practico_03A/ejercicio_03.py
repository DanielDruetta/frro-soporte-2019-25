# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from Practico_03A.ejercicio_02 import agregar_persona
from Practico_03A.ejercicio_01 import reset_tabla, engine, Persona
from sqlalchemy.orm import sessionmaker


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def borrar_persona(id_persona):
    persona=session.query(Persona).filter(Persona.idPersona==id_persona).first()
    if (persona is None):
        return False
    else:
        session.delete(persona)
        session.commit()
        return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
