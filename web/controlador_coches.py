from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_coche(marca, modelo, caballos,imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO coches(marca, modelo, caballos,imagen) VALUES (%s, %s, %s,%s)",
                       (marca, modelo, caballos,imagen))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un coche", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_coche_a_json(coche):
    d = {}
    d['id'] = coche[0]
    d['marca'] = coche[1]
    d['modelo'] = coche[2]
    d['caballos'] = coche[3]
    d['imagen'] = coche[4]
    return d

def obtener_coches():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, marca, modelo, caballos,imagen FROM coches")
            coches = cursor.fetchall()
            cochesjson=[]
            if coches:
                for coche in coches:
                    cochesjson.append(convertir_coche_a_json(coche))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los coches", file=sys.stdout)
        cochesjson=[]
        code=500
    return cochesjson,code

def obtener_coche_por_id(id):
    cochejson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, marca, modelo, caballos,imagen FROM coches WHERE id =" + id)
            coche = cursor.fetchone()
            if coche is not None:
                cochejson = convertir_coche_a_json(coche)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un coche", file=sys.stdout)
        code=500
    return cochejson,code


def eliminar_coche(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM coches WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un coche", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_coche(id, marca, modelo, caballos, imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE coches SET marca = %s, modelo = %s, caballos = %s, imagen=%s WHERE id = %s",
                       (marca, modelo, caballos, imagen,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un coche", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
