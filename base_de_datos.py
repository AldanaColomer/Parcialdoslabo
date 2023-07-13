import sqlite3

def crear_puntajes():
    with sqlite3.connect("base_de_datos.db") as conexion:
        try:
            sentencia = ''' create table puntajes
            (
                id integrer primary key autoincrement,
                nombre text, 
                puntaje integrer
            )
            ''' 
            conexion.execute(sentencia)
            print("Se creó la tabla de puntajes")
        except sqlite3.OperationalError:
            print("La tabla de puntajes ya es existente")
def insertar_puntajes(nombre: str, puntaje: int):
    with sqlite3.connect("base_de_datos.db") as conexion:
        try:
            conexion.execute("insert into puntajes(nombre, puntaje) values(?,?), (nombre, puntaje)")
            conexion.commit()
        except:
            print("Error al escribir la tabla")


def top_de_puntajes()->list:
    with sqlite3.connect("base_de_datos.db") as conexion:
        try:
            cursor = conexion.execute("Select * from puntajes order by puntaje desc limit 10")
            lista = cursor.fetchall()
        except:
            print("Error en los registros")
            lista = []
        return lista

def limpiar_tabla():
    with sqlite3.connect("base_de_datos.db") as conexion:
        cursor = conexion.execute("Select * from puntajes order by puntaje desc")
        lista = cursor.fetchall()
        if len(lista) > 10:
            for index,element in enumerate(lista):
                if(index > 9):
                    sentencia = "delete from puntajes where id= (?)"
                    id = lista[index][0]
                    caso = conexion.execute(sentencia, (id,))

