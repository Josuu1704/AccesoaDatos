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

for i in range(3):
    libro = input("Introduce tus libros: ")
    autor = input(("Introduce el auto de cada libro: "))
    disponible = input("Se encuentra dsiponible (s/n)")
    if disponible == "s":
        disponible = True
    else:
        disponible = False
