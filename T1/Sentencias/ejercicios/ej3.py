"""
Crearemos un programa en Python que gestione una pequeña biblioteca con las siguientes características:
    - Base de datos inicial
        - Crea un diccionario llamada biblioteca
        - Cada clave será el título de un libro (string) que será introducida por consola
        - Cada valor será un diccionario con la información:
            - autor -> string
            - disponible -> bool (True si está libre y False si está prestado)
        - Se solicitarán por consola todos los datos. Mínimo 3 libros.
        - Comprobaremos por consola si existe un libro. Si el libro no existe, muestra "El libro no existe en la biblio"
        - Si el libro existe, comprobaremos si está disponible (True o False).
        - Mostramos todos los libros y sus valores.
"""

biblioteca = {}

cantidad_libros = int(input("Cuantos libros quieres añadir: "))
print()

for i in range(cantidad_libros):
    libro = input(f"Intoduce el nombre del libro {i+1}: ")
    autor = input(f"Introduce el autor del libro {i+1}: ")
    disponibilidad = input(f"El libro {i + 1} esta disponible (s/n): ")

    biblioteca[libro] = {
        "autor": autor,
        "disponible": disponibilidad == "s"
     }
print()

existe_libro = input("Introduce el libro que quieras ver si existe: ")
if existe_libro in biblioteca:
    print(f"El libro {existe_libro} existe en la biblioteca.")
    if disponibilidad == "s":
        print("Esta disponible")
    else:
        print("No esta disponible")
else:

    print(f"El libro {existe_libro} no existe en la biblioteca.")
print()

print(biblioteca)
