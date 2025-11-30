from diccionario_juego import *
from estadisticas import *
from main_juego import *
from archivos_json import *   
import os


def main():

    usuario = None
    estadisticas = None         
    bandera = True

    while bandera:

        opcion = input("1. Iniciar sesión\n2. Registrarse\n3. Jugar Decifrar Palabra\n4. Ver Estadísticas\n5. Salir del programa\nElija una opción: ")

        match opcion:

            case "1":
                os.system("cls")
                usuario_login = login("usuariosprueba.json")

                if usuario_login != None:
                    usuario = usuario_login
                    estadisticas = cargar_estadisticas(usuario)

                    print(f"\nSesión iniciada como: {usuario['Usuario']}")
                else:
                    print("No se pudo iniciar sesión.")

            case "2":
                registrar_usuario("usuariosprueba.json")

            case "3":

                if usuario == None:
                    print("Debe iniciar sesión antes de jugar.")

                else:
                    limpiar_estadisticas(estadisticas)
                    resultado = jugar_juego(estadisticas)
                
                    mostrar_resultado_final(resultado, estadisticas)

                    actualizar_estadisticas(usuario, estadisticas)

            case "4":
                os.system("cls")
                if usuario == None:
                    print("Debe iniciar sesión para ver estadísticas.\n")
                else:
                    print(f"Estadisticas de {usuario["Usuario"]}:\n")

                    mostrar_diccionario(estadisticas)
                    print("\n")

            case "5":
                os.system("cls")
                print("Saliendo del programa...")
                bandera = False

            case _:
                print("ERROR... Elija una opción válida")

        os.system("pause")
        os.system("cls")


if __name__ == "__main__":
    main()