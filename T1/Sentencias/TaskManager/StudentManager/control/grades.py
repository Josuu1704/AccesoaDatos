def mediaNota(alumnos):
    if not alumnos:
        raise ValueError("No hay alumnos para calcular la media")
    return sum(alumno["nota"] for alumno in alumnos) / len(alumnos)

def mostrarSuspensos(alumnos):
    suspensos = []
    for alumno in alumnos:
        if alumno["nota"] < 5:
            suspensos.append(alumno)
    return suspensos

def mostrarAprobados(alumnos):
    aprobados =  []
    for alumno in alumnos:
        if alumno["nota"] >= 5:
            aprobados.append(alumno)
    return aprobados

