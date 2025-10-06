"""
Construir un programa que gestione personajes de
Marvel usando funciones y manejo de excepciones.

- Crea un diccionario vacio llamado marvel.
- Implementa las siguientes funciones con manejo
    de excepciones con raise cuando corresponda.

    - si alguien introduce como nombre
    un número arrojamos una excepción (raise)
    porque tiene que ser string.
    - Si el personaje existe arrojamos una excepción de
    KeyError.

- Implementa otra función para buscar un personaje.
    - Si existe, imprime el personaje.
    - Si no existe, arrojamos una excepción de KeyError.

- Implementar otra función para obtener (con return), el
    personaje con rating más alto.

- Hacer un panel de control tipo:
    - 1. Introducir usuario
    - 2. Comprobar si existe
    - 3. Ver personaje con mayor puntuación
    - 4. Salir
"""


marvel = {}


def mayor_rating():
    if len(marvel.keys()):
        aux = ""
        rt = 0
        for personaje, valor in marvel.items():
            if rt <= valor["rating"]:
                rt = valor["rating"]
                aux = personaje
            return marvel.get(aux)


def comprobar_no_existe(personaje):
    personaje = input("Introduce un personaje: ")
    #if marvel.get(personaje) is None:
    # raise KeyError("PErsonaje no existe")
    if personaje not in marvel.keys():
        raise KeyError("Personaje no exite")
    else:
        print(marvel.get(personaje))


def comprobar_nombre(nombre):
    try:
        number = float(nombre)
        raise TypeError("Error el nombre debe de ser un String")
    except ValueError:
        print("Nombre correcto. Insertemos...")


def comprobar_si_existe(personaje):
    if marvel.get(personaje) is not None: #Te verifica si el presonaje que introude ya existe. #Como el valor no es none o sea ya tiene una volor, Existe
        raise KeyError("Error: El nombre ya existe")

    #if personaje not in marvel.keys():  marvel.keys es una array [key1, key2, key3...]
    #    raise KeyError("Error: el nombre ya existe")


def insertar_personaje():
    try:
        nombre = input("Introduce un nombre del personaje: ")
        comprobar_nombre("nombre")
        comprobar_si_existe("nombre")

        alias = input("Introudce un alias del personaje: ")
        is_avaliable = input("Esta disponible (1. True / 2.False)")
        is_avaliable = is_avaliable == 1
        rating = float(input(""))
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)


def menu_fn():
    print()
    salir = False
    while not salir:
        print("---- MENU ----")
        print("1.Introducir usuario")
        print("2.Comproabsr si existe un personaje")
        print("3. Personaje con mayor rating")
        print("4. Salir")

        option = int(input("Introduce una opcion: "))
        if option == 1:
            insertar_personaje() #Funcion introducir un usuario
        elif option == 2:
            comprobar_no_existe() # Comporbacion si exite o no
        elif option == 3:
            pass # Ver personaje con > rating
        elif option == 4:
            salir = True #Salr del programa
        else:
            print("Opcion no valida")