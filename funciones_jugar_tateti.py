from Funciones_generales_comodin import *
from funciones_recorrer_comodin import * 
import os

grilla = crear_matriz(3, 3, "_")

def jugar_tateti(grilla: list):
    bandera = True
    maquina = True
    Ganador = 0

    while bandera == True:
        os.system("cls")
        mostrar_matriz(grilla)

        if estado_partida(grilla) == False:
            Ganador = 2
            bandera = False
            break
        
        if ingresar_jugada(grilla, 3) == False:
            os.system("cls")
            print("Error... vuelva a intentarlo más tarde")
            bandera = False
            break
        
        os.system("cls")

        if estado_partida(grilla) == False:
            mostrar_matriz(grilla)
            Ganador = 1
            break
        
        if tablero_lleno(grilla) == True:
            print("\nEmpate, no hay más espacios.")
            mostrar_matriz(grilla)
            bandera = False
            break

        while maquina:
            maquina = ingresar_maquina(grilla)
        maquina = True
    
    return Ganador
        
def ingresar_jugada(grilla: list, reintentos: int = 3):
    contador = 0
    ingreso_valido = True

    fila = get_int("En qué fila queres ingresar: ", "Error, esa fila no existe", 0, 2, 3)
    columna = get_int("En qué columna queres ingresar: ", "Error, esa columna no existe", 0, 2, 3)

    while grilla[fila][columna] != "_" and contador < reintentos:
        contador += 1

        if contador < reintentos:
            print(f"La casilla está ocupada. Te quedan {reintentos - contador} reintentos.")
            fila = get_int("Vuelva a ingresar otra fila: ", "Error, esa fila no existe", 0, 2, 3)
            columna = get_int("Vuelva a ingresar otra columna: ", "Error, esa columna no existe", 0, 2, 3)
        else:
            print("Te quedaste sin reintentos 💀")
            ingreso_valido = False

    if ingreso_valido == True:
        grilla[fila][columna] = "X"

    return ingreso_valido
        
#jugar_tateti(grilla)