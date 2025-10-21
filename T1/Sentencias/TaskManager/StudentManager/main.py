from T1.Sentencias.TaskManager.StudentManager import *

salir = False

while not salir:
    print("\n~~~~ GESTIÓN DE ALUMNOS ~~~~")
    print("1. Crear alumno")
    print("2. Ver todos los alumnos")
    print("3. Borrar alumno por ID")
    print("4. Borrar alumno por nombre")
    print("5. Ver media de la clase")
    print("6. Ver aprobados")
    print("7. Ver suspensos")
    print("8. Salir")

    opcion = opcionMenu()

    if opcion == "1":
        nombre = pedirNombre()
        nota = pedirNota()
        try:
            mensaje = crearAlumno(nombre, nota)
            print(mensaje)
        except ValueError as e:
            print(e)

    elif opcion == "2":
        verAlumno()

    elif opcion == "3":
        id_alumno = pedirId()
        try:
            mensaje = remove_Id(id_alumno)
            print(mensaje)
        except ValueError as e:
            print(e)

    elif opcion == "4":
        nombre = pedirNombre()
        try:
            mensaje = borrarPorNombre(nombre)
            print(mensaje)
        except ValueError as e:
            print(e)

    elif opcion == "5":
        try:
            media = mediaNota(alumnos)
            print(f"La media de la clase es: {media:.2f}")
        except ValueError as e:
            print(e)

    elif opcion == "6":
        aprobados = mostrarAprobados(alumnos)
        if not aprobados:
            print("No hay alumnos aprobados.")
        else:
            for alumno in aprobados:
                print(f"{alumno['nombre']} | Nota: {alumno['nota']}")

    elif opcion == "7":
        suspensos = mostrarSuspensos(alumnos)
        if not suspensos:
            print("No hay alumnos suspensos")
        else:
            for alumno in suspensos:
                print(f"{alumno['nombre']} | Nota: {alumno['nota']}")

    elif opcion == "8":
        salir =  True
        print("Saliendo del programa...")

    else:
        print("Opcion invalida...")
