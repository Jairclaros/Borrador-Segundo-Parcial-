from estadisticas import *
from funciones_mostrar import *
from main_juego import *

def ver_estadisticas(usuario, estadisticas):
    if usuario == None:
        print("Debe iniciar sesión para ver estadísticas.\n")
    else:
        print(f"Estadisticas de {usuario['Usuario']}:\n")
        mostrar_diccionario(estadisticas)
        print("\n")


def ejecutar_juego(usuario, estadisticas):
    if usuario == None:
        print("Debe iniciar sesión antes de jugar.")
    else:
        limpiar_estadisticas(estadisticas)
        resultado = jugar_juego(estadisticas)

        mostrar_resultado_final(resultado, estadisticas)

        actualizar_estadisticas(usuario, estadisticas)