import random

def rebanar(cadena: str, inicio: int, finalizacion: int) -> str:
    """_summary_

    Args:
        cadena (str): String recibido por parametro.
        inicio (int): Entero que recibido por parametro que marca el inicio.
        finalizacion (int): Entero recibido por parametro que marca la finalizacion

    Returns:
        str: La funcion retorna un nuevo string, recortando el anterior desde el inicio hasta la finalizacion. 
    """
    cadena_auxiliar = ""
    for caracter in range(inicio, finalizacion):
        cadena_auxiliar += cadena[caracter]

    return cadena_auxiliar


def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras descubiertas por el usuario recibida por parametro.

    Returns:
        list: Returna una lista sin elementos repetidos
    """

    palabras_total = []

    for i in range(len(palabras_asociadas)):
        palabras_total.append(palabras_asociadas[i])

    for i in range(len(palabras_descubiertas)):
        repetido = False

        for j in range(len(palabras_total)):
            if palabras_descubiertas[i] == palabras_total[j]:
                repetido = True
                break

        if repetido == False:
            palabras_total.append(palabras_descubiertas[i])

    return palabras_total


def ocultar_palabras(palabras_asociadas: list, palabras_descubiertas: list):
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras decubiertas por el usuario recibida por parametro.

    Returns:
        list: La funcion retorna una nueva lista modificada utilizando ambas lista. Modifica cada elemento de las listas para agregar "_" a cada indice de los elementos.
    """

    palabras_total = listar_palabras(palabras_asociadas, palabras_descubiertas)

    ocultas = []

    for i in range(len(palabras_total)):
        encontrada = False

        for j in range(len(palabras_descubiertas)):
            if palabras_total[i] == palabras_descubiertas[j]:
                encontrada = True
                break

        if encontrada == True:
            ocultas.append(palabras_total[i])
        elif encontrada == False:
            ocultas.append("_" * len(palabras_total[i]))

    return ocultas


def seleccionar_string_aleatoria(lista: list) -> str:
    """_summary_

    Args:
        lista (list): Lista recibida por parametro. 

    Returns:
        str: La funcion toma un elemento aleatorio de la lista, lo guarda en una variable y lo retorna.
    """

    indice = random.randint(0, len(lista) - 1)

    indice_string = lista[indice]

    return indice_string