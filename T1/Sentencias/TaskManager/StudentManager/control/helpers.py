def pedirNombre():
    nombre = input("Introduce el nombre del alumno: ")
    return nombre

def pedirNota():
    nota = float(input("Introduce la nota del alumno (0-10): "))
    return nota

def pedirId():
    id_alumno = input("Introduce el ID del aluumno: ")
    if not id_alumno:
        print("El Id no puede esta vacio.")
    return id_alumno

def opcionMenu():
    opcion = input("Elige la operacion que quieras realizar: ")
    return opcion
