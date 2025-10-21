from Clases.ej1corregido import Student

estudiantes = []

salir = False
while not salir:
    nombre = input("s: Salir | Introduce un nombre: ")
    if nombre != "s":
        try:
            estudiante = Student(nombre)
            estudiantes.append(estudiante)
        except ValueError as e:
            print(e)
    else:
        salir = True

for estudiante in estudiantes:
    print(estudiante)