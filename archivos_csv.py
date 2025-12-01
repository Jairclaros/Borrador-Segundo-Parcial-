from diccionario_juego import *
from funciones_csv import *
from especificas import *


def validar_crear_csv(bandera: bool):

    if bandera == False:
        print("El CSV fue creado con exito !!!")
    else:
        print("No se pudo crear el CSV.")


def crear_csv(diccionario: dict):

    diccionario_copia = copiar_lista(diccionario)
    hubo_error = False

    try:
        with open("diccionario_juego.csv", "w", encoding="utf8") as archivo:

            for i in range(5):
                nivel = i + 1

                for j in range(3):
                    try:
                        lista_letras = elegir_letras_csv(diccionario_copia)
                        lista_palabras = elegir_palabras_csv(diccionario_copia, lista_letras)

                        datos_validos = True

                        if not lista_letras:
                            datos_validos = False

                        if not lista_palabras:
                            datos_validos = False

                        if datos_validos:

                            recorrer_palabras = recorrer_lista_palabras(lista_palabras)
                            recorrer_letras = recorrer_lista_letras(lista_letras)

                            eliminar_lista_csv(diccionario_copia, lista_letras, lista_palabras)

                            linea = f"{nivel},{recorrer_letras},{recorrer_palabras}\n"
                            archivo.write(linea)

                        else:
                            hubo_error = True

                    except:
                        hubo_error = True

    except:
        hubo_error = True

    validar_crear_csv(hubo_error)
