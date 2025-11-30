import json

def crear_archivo_json():
    """_summary_

    Crea o valida la existencia del archivo Json

    """
    try:
        with open("usuariosprueba.json", "r") as archivo:
            contenido = archivo.read()

        if contenido == "":
            with open("usuariosprueba.json", "w") as archivo:
                archivo.write("[]")

    except:
        with open("usuariosprueba.json", "w") as archivo:
            archivo.write("[]")

def leer_json(path: str):
    """_summary_

    Lee y retorna el contenido del Json 

    Returns:
        list: Lista de usuarios del archivo Json
    """
    datos = []  

    try:
        with open(path, "r") as archivo:
            datos = json.load(archivo)
    except:
        with open(path, "w") as archivo:
            archivo.write("[]")
        datos = [] 

    return datos

def guardar_json(lista: list, path: str):
    """_summary_

    Guarda una lista de usuarios en el archivo Json
    
    Args:
        lista (list): Lista que se guarda en el Json
    """
    try:
        with open(path, "w") as archivo:
            json.dump(lista, archivo, indent=4)
    except:
        print("Error al guardar el archivo JSON.")


def registrar_usuario(path: str):
    """_summary_

    Registra / Crea un nuevo usuario en el archivo Json 

    Returns:
        bool: Retorna True si el usuario se creo correctamente
              Retorna None si ya existia el usuario o paso un error
    """
    resultado = None
    usuarios = leer_json(path)

    print("\n--- REGISTRAR NUEVO USUARIO ---")

    nombre = input("Ingrese un nombre de usuario: ")

    existe = False
    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == nombre:
            existe = True

    if existe:
        print("Ese usuario ya existe. Elija otro.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        nuevo_usuario = {
            "Usuario": nombre,
            "Contrasena": contrasena,
            "Puntuacion Total" : 0,
            "Ingresos incorrectos" : 0,
            "Tiempo restante total en segundos" : 0,
            "Tiempo entre niveles" : 0,
            "Tiempo promedio entre niveles" : 0
        }

        usuarios.append(nuevo_usuario)
        guardar_json(usuarios, path)
        print("Usuario registrado con éxito.")
        resultado = True

    return resultado   


def login(path: str):
    """_summary_

    Verifica el usuario y contrasena para iniciar sesion

    Returns:
        dict: Retorna el diccionario del usuario, si ingreso bien los datos
              Retorna None si no coinciden los datos
    """
    resultado = None
    usuarios = leer_json(path)

    print("INICIAR SESION:\n")

    nombre = input("Usuario: ")
    contrasena = input("Contraseña: ")

    encontrado = None
    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == nombre and usuarios[i]["Contrasena"] == contrasena:
            encontrado = usuarios[i]

    if encontrado != None:
        print("Inicio de sesión exitoso.\n")
        resultado = encontrado
    else:
        print("Usuario o contraseña incorrectos.\n")

    return resultado  

def actualizar_usuario_estadisticas(usuario_modificado: dict, path: str):
    """_summary_

    Actualiza las estadisticas de un usuario en el archivo Json

    Args:
        usuario_modificado (dict): Diccionario del usuario con sus datos modificados

    Returns:
        bool: Retorna True si se actualizaron bien las estadisticas del usuario
              Retorna None si el usuario no existe en el archivo
    """
    usuarios = leer_json(path)
    indice = -1 
    resultado = None

    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == usuario_modificado["Usuario"]:
            indice = i

    if indice != -1:
        usuarios[indice] = usuario_modificado
        guardar_json(usuarios, path)
        resultado = True
    else:
        print("No se pudo actualizar el usuario porque no existe.")

    return resultado

