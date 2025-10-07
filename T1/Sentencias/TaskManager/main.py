"""

Crear un proyecto llamado task_manager con 3 archivos.
    -
main.py
 -> Principal
    -
functions.py
 -> contiene las funciones add_task, remove_task, show_tasks
    -
helpers.py
 -> contiene ask_number() aquí se pide y se valida con try/except

El programa debe importar las funciones desde los módulos y ejecutar un menú como los que hemos hecho,
pero organizando mejor el código.

"""

from TaskManager import *

task_list = {}

val = True
while val:
    print("Intoduce una opcion: ")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tarea")
    print("4. Salir")
    option = int(input(">>"))

    if option == 1:
        try:
            task = ask_number(task_list, 1)
            task_list = add_task(task, task_list)
        except ValueError as e:
            print(e)
    elif option == 2:
        try:
            task = ask_number(task, task_list)
        except ValueError as e:
            print(e)
    elif option == 3:
        show_task(task_list)
    elif option == 4:
        val = False
    else:
        print("OPcion no valido.")
