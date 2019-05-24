# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from Practico_03A.ejercicio_02 import agregar_persona
from Practico_03A.ejercicio_06 import reset_tabla, Peso
from Practico_03A.ejercicio_04 import buscar_persona
from sqlalchemy.orm import sessionmaker
from Practico_03A.ejercicio_01 import engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def buscar_peso(id_persona,fecha):
    pesaje=session.query(Peso).filter(Peso.idPersona==id_persona, Peso.fecha > fecha).first()
    if (pesaje is None):
        return False
    else:
        return True

def agregar_peso(id_persona, fecha, peso):
    encontrado=buscar_persona(id_persona)
    if encontrado is False:
        return False
    else:
        existe_pesaje=buscar_peso(id_persona,fecha)
        if existe_pesaje is True:
            return False
        else:
            oper = Peso()
            oper.idPersona=id_persona
            oper.fecha=fecha
            oper.peso=peso
            session.add(oper)
            session.commit()
            return oper.idPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 30), 85)

if __name__ == '__main__':
    pruebas()
