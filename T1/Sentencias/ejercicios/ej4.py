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

    alias = input(f"Intoduce el alias del superheroe {i+1}: ")
    team = input(f"Introduce el equipo al que pertene el superheroe {i+1}: ")

    power = []
    poder1 = input(f"Introduce los poderes del superherore {i+1}: ")
    poder2 = input(f"Introduce los poderes del superherore {i+1}: ")
    power.append(poder1)
    power.append(poder2)

    isAvaible = input(f"Introduce si esta disponible el superheroe {i+1} (s/n): ")
    valoration = float(input(f"Intruduce la valoracion del superherore {i+1}: "))

    marvel[nombre]={
        "alias": alias,
        "team": [team],
        "power": [power],
        "Disponible": isAvaible == "s",
        "valoracion": valoration
    }

print()
for clave, valor in marvel.items():
    if valor["Disponible"]:
        print(f"")


print()
print(marvel)
