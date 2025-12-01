from funciones_csv import *
import re

def validar_reconstruir_diccionario(bandera: bool):

    if bandera == False:
        print("Diccionario reconstruido para el juego con exito !!!")
    else:
        print("No se puedo reconstruir el diccionario para el juego.")


def crear_estructura_base():

    lista = []
    lista_banderas = [False, False, False]

    for i in range(5):
        lista.append({
            "nivel": i + 1,
            "estado_comodines": lista_banderas,
            "partidas": []
        })

    return lista


def extraer_letras(cadena: str):
    letras = []

    for i in range(len(cadena)):
        c = cadena[i]
        if c != " ":
            letras.append(c)

    return letras


def validar_nivel(texto: str):

    nivel_valido = None

    try:
        nivel = int(texto)
        if 1 <= nivel and nivel <= 5:
            nivel_valido = nivel
    except:
        nivel_valido = None

    return nivel_valido


def procesar_linea(linea: str):

    resultado = {"error": False, "nivel": None, "partida": None}

    try:
        registro = re.split(",|\n", linea)

        if len(registro) < 3:
            resultado["error"] = True
        else:
            nivel = validar_nivel(registro[0])

            if nivel == None:
                resultado["error"] = True
            else:
                letras = extraer_letras(registro[1])
                palabras = armar_palabras("", registro[2])

                resultado["nivel"] = nivel
                resultado["partida"] = {
                    "letras": letras,
                    "palabras": palabras
                }

    except:
        resultado["error"] = True

    return resultado


def reconstruir_diccionario(path: str) -> list:

    lista_final = crear_estructura_base()
    hubo_error = False

    try:
        with open(path, "r", encoding="utf8") as archivo:

            for linea in archivo:
                resultado = procesar_linea(linea)

                if resultado["error"]:
                    hubo_error = True
                else:
                    nivel = resultado["nivel"]
                    partida = resultado["partida"]
                    lista_final[nivel - 1]["partidas"].append(partida)

    except:
        hubo_error = True

    validar_reconstruir_diccionario(hubo_error)

    return lista_final