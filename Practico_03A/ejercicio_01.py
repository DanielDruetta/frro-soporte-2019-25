# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float

Base=declarative_base()

class Persona(Base):
        __tablename__='TablaPersona'
        idPersona = Column(Integer, primary_key=True, autoincrement=True)
        nombre = Column(String)
        fechaNacimiento = Column(String)
        dni = Column(Integer)
        altura = Column(Float)

engine=create_engine('sqlite:///sqlalchemy_tp3a.db')
Base.metadata.bind = engine

def crear_tabla():
    Persona.__table__.create()

def borrar_tabla():
    Persona.__table__.drop()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


