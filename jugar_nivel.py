from niveles import *
import os

def mostrar_encabezado(nivel: int, ronda: int):
    os.system("cls")
    print(f"\nNivel {nivel}\n")
    print(f"Ronda {ronda} / 3\n")


def jugar_nivel(diccionario: dict, nivel_actual: int, estadisticas: dict, contador: int) -> bool:
    """_summary_

    Juega las 3 rondas correspondientes al nivel del juego, mostrando los comodines disponibles.
    Y muestra en que nivel y ronda esta jugando el usuario

    Args:
        diccionario (dict): Diccionario del juego que contiene todas las palabras, niveles, letas, etc del juego
        nivel_actual (int): Numero del nivel que se esta jugando
        estadisticas (dict): Diccionario donde se guardan las estadisticas
        contador (int): Contador que cuenta el total de rondas jugas 

    Returns:
        bool: True si el jugador completa las 3 rondas del nivel,
              False si no completa el nivel.
    """

    rondas = 0
    completar_nivel = True

    datos_nivel = preparar_nivel(diccionario, nivel_actual)
    partidas_temporales = datos_nivel["partidas_temporales"]
    estado_comodines = datos_nivel["estado_comodines"]

    while rondas < 3:

        mostrar_encabezado(nivel_actual, rondas + 1)
        mostrar_comodines(estado_comodines)

        resultado = procesar_ronda(diccionario,nivel_actual,estadisticas,contador,partidas_temporales)

        bandera = resultado["bandera"]
        contador = resultado["contador"]

        if bandera:
            os.system("pause")
            rondas += 1
        else:
            completar_nivel = False
            rondas = 3

    os.system("cls")

    return completar_nivel