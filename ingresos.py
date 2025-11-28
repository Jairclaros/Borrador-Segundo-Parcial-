from combinar import *

def actualizar_ocultas(lista_palabras: list, palabras_ingresadas: list, lista_ubicar: list, lista_revelar: list, estado_comodines: list) -> list:
    """_summary_

    Modifica la lista de palabras ocultas, y aplica el efecto del comodin ubicar letra
    si es activado
    
    Funciona en dos etapas:
        1. Oculta normalmente las palabras no adivinadas.
        
        2. Si el comodín 'Ubicar letra' está activo, combina la ocultación
        con la letra ubicada usando `combinar_listas_ubicar`.

    Args:
        lista_palabras (list): Lista original de todas las palabras de la ronda.
        palabras_ingresadas (list): Lista de palabras ya adivinidadas.
        lista_ubicar (list): Lista donde se guarda el resultados del segundo comodin.
        lista_revelar (list): Lista donde se guarda el resultados del primer comodin.
        estado_comodines (list): Lista que indica si el comodín fue usado.

    Returns:
        list: la funcion retorna la lista combinada con el efecto del comodin. Si el comodin ya fue utilizado solo retorna una lista de palabras ocultas.
    """

    lista_ocultas_base = ocultar_palabras(lista_palabras, palabras_ingresadas)

    combinada = lista_ocultas_base

    if estado_comodines[0] and not estado_comodines[1]:
        combinada = combinar_listas_ubicar(lista_revelar, lista_ocultas_base, lista_palabras)

    if estado_comodines[1] and not estado_comodines[0]:
        combinada = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)

    if estado_comodines[0] and estado_comodines[1]:

        mitad = combinar_listas_ubicar(lista_revelar, lista_ocultas_base, lista_palabras)
        ubicar = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)
        combinada = combinar_listas(ubicar, mitad, lista_palabras)

    return combinada


def obtener_ingreso(estado_comodines: list) -> str:
    """_summary_

    Args:
        estado_comodines (list): Lista de banderas recibida por parametro.

    Returns:
        str: La funcion le pide un dato al usuario y dependiendo del estado de la bandera, le mostrará un mensaje avisandole que puede usar un comodin.
             Finalmente, retorna el dato ingresado por el usuario.
    """

    if estado_comodines[0] == False and estado_comodines[1] == False and estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra. [1] o [2] o [3] para Comodines: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == False and estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra, [1] o [2] para usar Revelar o Ubicar: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == True and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra, [1] o [3] para usar Revelar o Ta-te-ti: ")
    
    elif estado_comodines[0] == True and estado_comodines[1] == False and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra, [2] o [3] para usar Ubicar Letras o Ta-te-ti: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == True and  estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra, [1] para usar Revelar Palabra: ")

    elif estado_comodines[0] == True and estado_comodines[1] == False and  estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra o [2] para usar Ubicar Letras: ")

    elif estado_comodines[0] == True and estado_comodines[1] == True and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra o [3] para usar Comodin Ta-te-ti: ")
    
    else:
        ingreso = input("Ingrese una palabra: ")

    return ingreso
