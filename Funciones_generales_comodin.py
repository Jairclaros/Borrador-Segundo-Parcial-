from funciones_recorrer_comodin import *
import random


def crear_matriz(filas: int, columnas: int, valor_inicial: any):
    matriz = []
    for _ in range(filas):
        una_fila = [valor_inicial] * columnas

        matriz += [una_fila]
    
    return matriz


def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print()


# def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:

#     numero_valido = int(input(mensaje)) - 1
 
#     while numero_valido < minimo or numero_valido > maximo:
        
#         if reintentos == 0:
#             print("Error... vuelvalo a intentar mas tarde")
#             return None
#         else:
#             print(f"Numero invalido, le quedan {reintentos} reintentos")
#             numero_valido = int(input(mensaje_error))
#             reintentos -= 1 
    
    
#     return numero_valido

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    """summary

    Args:
        mensaje (str): Es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error (str): Mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): Valor mínimo admitido (inclusive)
        maximo (int): Valor máximo admitido (inclusive)
        reintentos (int): Cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int | None: Si luego de varios reintentos, el dato no se encuentra entre el minimo y el maximo, la funcion retornará None. Caso contrario, retornará el numero ingresado.
    """

    intentos = 0
    resultado = None

    while intentos < reintentos:
        cadena = input(mensaje)

        if validar_numero_entero(cadena):
            numero = int(cadena) - 1
            if minimo <= numero and numero <= maximo:
                resultado = numero
                break
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)

        intentos += 1

    return resultado

def validar_numero_entero(cadena: str) -> bool:
    """summary

    Args:
        cadena (str): Cadena ingresada por parametro que sera recorrida elemento por elemento.

    Returns:
        bool: retorna un booleano.
    """

    bandera = True

    if len(cadena) == 0:
        bandera = False

    for i in range(len(cadena)):
        caracter = cadena[i]
        codigo = ord(caracter)

        if i == 0 and (caracter == '+' or caracter == '-'):
            bandera = True
        elif not (48 <= codigo and codigo <= 57):
            bandera = False
            break

    return bandera

def tablero_lleno(grilla: list) -> bool:
    lleno = True

    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if grilla[i][j] == "_":
                lleno = False

    return lleno


def ingresar_maquina(grilla: list):

    maquina = True

    while maquina:
            fila_aleatoria = random.randint(0,2)
            columna_aleatoria = random.randint(0,2)

            if grilla[fila_aleatoria][columna_aleatoria] == "_":
                grilla[fila_aleatoria][columna_aleatoria] = "O"
                maquina = False

    return maquina


def estado_partida(grilla: list) -> bool:
    seguir = True

    if seguir == True and verificar_filas(grilla) == False:
        seguir = False

    if seguir == True and verificar_columnas(grilla) == False:
        seguir = False

    if seguir == True and verificar_diagonal(grilla) == False:
        seguir = False

    if seguir == True and verificar_diagonal_inversa(grilla) == False:
        seguir = False

    return seguir
