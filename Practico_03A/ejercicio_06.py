# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from Practico_03A.ejercicio_01 import borrar_tabla, crear_tabla, Persona
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy import create_engine

Base=declarative_base()

class Peso(Base):
    __tablename__ = 'PersonaPeso'
    idPeso = Column(Integer, primary_key=True, autoincrement=True)
    idPersona = Column(Integer, ForeignKey(Persona.idPersona))
    fecha = Column(String)
    peso = Column(Float)

def crear_tabla_peso():
    Peso.__table__.create()

def borrar_tabla_peso():
    Peso.__table__.drop()

engine=create_engine('sqlite:///sqlalchemy_tp3a.db')
Base.metadata.bind = engine

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


