from especificas import *
from juego_muestra import *

def preparar_nivel(diccionario, nivel_actual):
    """
    Prepara y devuelve todos los datos necesarios para jugar un nivel.
    Devuelve un único diccionario.
    """

    nivel_diccionario = diccionario[nivel_actual - 1]

    partidas_temporales = copiar_lista(nivel_diccionario["partidas"])
    estado_comodines = nivel_diccionario["estado_comodines"]

    datos = {
        "partidas_temporales": partidas_temporales,
        "estado_comodines": estado_comodines
    }

    return datos


def procesar_ronda(diccionario, nivel_actual, estadisticas, contador, partidas_temporales):
    """
    Ejecuta la ronda de juego sin mostrar nada en pantalla.
    Devuelve un único diccionario con:
    - bandera: bool
    - contador: int actualizado
    """

    bandera = jugar_palabras(diccionario, nivel_actual, estadisticas, contador, partidas_temporales)

    nuevo_contador = contador
    if bandera:
        nuevo_contador = contador + 1

    datos = {
        "bandera": bandera,
        "contador": nuevo_contador
    }

    return datos

