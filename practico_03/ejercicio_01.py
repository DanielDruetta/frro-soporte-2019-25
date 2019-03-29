# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
conexion = sqlite3.connect(basedatos.db)
c=conexion.cursor()
def crear_tabla():
    c.execute('''CEATE TABLE persona
                (idPersona integer PRIMARY KEY AUTOINCREMENT,
                
                )''')


def borrar_tabla():
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


