import random

alumnos = []

def crearAlumno(nombre,nota):
    if not nombre:
        raise ValueError("El nombre no puede estar vacio")
    if nombre.isnumeric():
        raise ValueError("El nombre no puede ser un numero")

    id_alumno = generarId()
    while comprobarID(alumnos, id_alumno):
        id_alumno = generarId()

    alumno = {
        "student_id": id_alumno,
        "nombre": nombre,
        "nota": nota
    }

    alumnos.append(alumno)
    return f"Alumno {nombre} ID:{id_alumno}"

def generarId():
    return random.randint(1000, 9999)


def comprobarID(alumnos, id_alumno):
    for alumno in alumnos:
        if alumno["student_id"] == id_alumno:
            return True
    return False


def remove_Id(id_alumno):
    for alumno in alumnos:
        if alumno["student_id"] == id_alumno:
            if alumno["nota"] < 5:
                alumnos.remove(alumno)
                return f"Alumno {id_alumno} eliminado"
            else:
                raise ValueError("No se puede borrar alumnos con notas mayores a 5")
    raise ValueError("No se encontro ningun alumno con ese ID")

def borrarPorNombre(nombre):
    for alumno in alumnos:
        if alumno["nombre"] == nombre:
            if alumno["nota"] < 5:
                alumnos.remove(alumno)
                return f"Alumnos {nombre} eliminado"
            else:
                raise ValueError ("No se pueden borrar alumno con mas nota")
    raise ValueError("No se encuetnra al alumno ")

def verAlumno():
    if not alumnos:
        print("No hay alunmos registrados")
    else:
        for alumno in alumnos:
            print(f"Nombre: {alumno['nombre']} | Nota: {alumno['nota']} ")


