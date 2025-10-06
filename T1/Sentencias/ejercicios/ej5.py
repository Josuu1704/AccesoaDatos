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


MARVEL = {}


def mayor_rating():
    if len(MARVEL.keys()) > 0:
        aux = ""
        rt = 0
        for personaje, valor in MARVEL.items():
            if rt <= valor["rating"]:
                rt = valor["rating"]
                aux = personaje
        return MARVEL.get(aux)
    else:
        return "No hay personajes"


def comprobar_no_existe():
    personaje = input("\nIntroduce un personaje: ")
    # if MARVEL.get(personaje) is None:
    #     raise KeyError("Personaje no existe")
    if personaje not in MARVEL.keys():
        raise KeyError("Personaje no existe")
    else:
        print(MARVEL.get(personaje))
        # print(MARVEL[personaje])


def comprobar_nombre(nombre):
    try:
        number = float(nombre)
        raise TypeError("Error: El nombre debe ser un str")
    except ValueError:
        print("Nombre correcto. Insertemos...")


def comprobar_si_existe(personaje):
    if MARVEL.get(personaje) is not None:
        raise KeyError("Error: El nombre ya existe")
    # if personaje not in MARVEL.keys(): ### MARVEL.keys() es un array [key1, key2, key3, ...]
    #     raise KeyError("Error: El nombre ya existe")


def insertar_personaje():
    try:
        nombre = input("\nIntroduce un nombre del personaje: ")
        comprobar_nombre(nombre)
        comprobar_si_existe(nombre)

        alias = input("Introduce un alias del personaje: ")
        is_available = input("Está disponible? (1 - True / 2- False): ")
        is_available = is_available == 1
        rating = float(input("Rating (0-10): "))

        MARVEL[nombre] = {
            "alias": alias,
            "team": [],
            "powers": [],
            "isAvailable": is_available,
            "rating": rating
        }

        for i in range(1):
            team = input("Introduce un equipo: ")
            MARVEL[nombre]["team"].append(team)

        for i in range(1):
            power = input("Introduce un poder: ")
            MARVEL[nombre]["powers"].append(power)

    except KeyError as e:
        print(e)
    except TypeError as e:
        print(e)


def menu_fn():
    salir = False
    while not salir:
        print("\n1 - Introducir personaje")
        print("2 - Comprobar si existe un personaje")
        print("3 - Personaje con mayor rating")
        print("4 - Salir")
        opt = int(input("Introduce una opción: "))
        if opt == 1:
            insertar_personaje()  # -> Introducir un personaje
        elif opt == 2:
            # Comprobación si existe o no
            try:
                comprobar_no_existe()
            except KeyError as e:
                print(e)
        elif opt == 3:
            # Ver personaje con > rating
            print(mayor_rating())
        elif opt == 4:
            salir = True  # Salir del programa
        else:
            print("Opción no válida")


def main():
    menu_fn()
    # print(MARVEL.get("tony stark"))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Programme interrupted.")
