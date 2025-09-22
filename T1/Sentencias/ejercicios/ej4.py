"""
Construiremos un programa en Python que gestione un pequeño registro de personajes y equipos de Marvel.
    - Crea un diccionario llamado marvel donde cada clave sea un nombre de un personaje y su valor sea otro diccionario.
    - El valor debe de tener los siguietnes elementos:
        - alias -> nombre del superheroe.
        - team -> sera un array unidimensional. Valores añadidos por consola. "Avenger", "X-Men"
        - powers -> lista de poderes (array de string)
        - isAvaible -> Si esta disponible o no (True o False)
        - valoracion -> valoracion del personaje 0.0 al 100 (float)

    Incluir al menos tres personajes. Todos se introduce de fomra manual

    - Mostrar todos los personajes introducidos
    - Mostrar todos los nombres de los personajes que esten disponibles
    - Buscar un personaje es el que tiene mas rating de todos los introducidos
    - Decir que personaje es el que tine mas rating de todos los introducidos
"""

marvel = {}
cantidad = int(input("Cuantos superheroes quieres introducir: "))
print()

for i in range(cantidad):
    nombre = input(f"Introduce el nombre del superheroe {i+1}: ")

    alias = input(f"Introduce el alias del supeheroe {i+1}: ")
    team = input(f"Introduce el team del supeheroe {i+1}: ")

    print(marvel)
